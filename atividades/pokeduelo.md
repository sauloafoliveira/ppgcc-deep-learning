
![logo](../ppgc_logo.png)

---

Aprendizagem Profunda – 2025.1

**Prof. Dr. Saulo Oliveira**

Data de Entrega: Uma semana após a definição.

Meio de Entrega: ```Colab com simulações```.

---

## Dataset: Sprites da pokeapi.co




O primeiro filme do Pokémon também foi a primeira ida ao cinema, nos anos 2000, lá no **Cinema São Luiz**, hoje, **Cineteatro São Luíz**. Uma tia minha, levou uma comitiva de 05 sobrinhos para assistir ao longa-metragem e depois lanchar no McDonalds da Rua Barão do Rio Branco. Nostalgia!

![pokemon-capa](https://upload.wikimedia.org/wikipedia/pt/1/1c/Mewtwo_Contra-Ataca.jpg) 


Pokémon moldou toda a minha infância e foi a primeira coisa que me veio à mente quando procurava um conjunto de dados interessante de pequenas imagens. Eu mesmo faço o uso da [PokeAPI](pokeapi.co) nas disciplinas de Desenvolvimento WEB e Programação para Dispositivos móveis. Eu descobri e explorei este mundo principalmente jogando uma variedade de diferentes videogames tradicionais de Pokémon, começando inicialmente no ```Pokémon Red``` (Geração 1) e terminando no ```Pokémon Emerald``` (Geração 3), tudo via emuladores -- infância reduzida em termos de recursos financeiros e telemáticos. 

![fitas](https://3.bp.blogspot.com/-GDocLuzl2Zs/W4LUP3HidWI/AAAAAAAAA9Q/cn8CZbPJmewddJ235T98J1h8IHfciVjvQCLcBGAs/s1600/gold-silver.jpg)


Confesso que nem entendia direito o que o Mewtwo falava enquanto filosofava sobre a sua existência. Para quem não lembra, o Mewtwo era um Pokémon clonado a partir do DNA do Mew. Deixo aqui algumas de suas mais célebres falas:

> As circunstâncias do nascimento de alguém são irrelevantes. É o que você faz com o dom da vida que determina quem você é. 

> Aqueles que me criaram nunca perguntaram se eu queria existir. Por isso, eu não posso perdoá-los.

> Nós temos muita coisa em comum, a mesma terra, o mesmo ar, o mesmo céu. Talvez se começássemos a olhar para as coisas que temos em comum ao invés de diferente… Bom, quem sabe?

![mew-two](https://media.tenor.com/xJC6LftJjagAAAAC/mewtwo-fire.gif)



## O que é o trabalho?

**Poké-Duelo**

Desenvolver um modelo que, **dado um par de imagens de Pokémon**, **classifique o resultado do duelo** como:

- `Vitória` (1º Pokémon vence)
- `Empate` (poderes equivalentes)
- `Derrota` (2º Pokémon vence)

A ideia é que o modelo **aprenda representações visuais úteis (via CNN)** e **internalize regras de vantagem de tipo + poder ofensivo aproximado**.

### O que é vantagem de tipos?
A vantagem de tipos em Pokémon é uma mecânica fundamental que define como eficazes os ataques de um Pokémon são contra outro, com base em seus tipos elementares (fogo, água, grama, etc). É uma matriz de relações que afeta o dano causado, e foi inspirada em lógica de pedra-papel-tesoura, mas com dezenas de combinações.
Cada Pokémon e cada ataque têm um ou dois tipos. No nosso caso, vamos simplificar que o cada Pokémon ataca somente com os tipos que ele possui.

As principais **multiplicações de dano** são:

| Eficácia           | Multiplicador     | Exemplo                              |
| ------------------ | ----------------- | ------------------------------------ |
| Super eficaz       | ```×2```          | Ataque de Água em Pokémon de Fogo    |
| Pouco eficaz       | ```×0.5```        | Ataque de Fogo em Pokémon de Água    |
| Sem efeito (imune) | ```×0```          | Ataque de Normal em Pokémon Fantasma |
| Normalmente eficaz | ```×1```          | Tipos sem relação especial           |

Se o Pokémon defensor tem dois tipos, os multiplicadores se combinam. Imagine um Pokémon Lutador atacando um Pokémon do tipo Normal/Voador:

- Contra Normal: ```×2```
- Contra Voador: ```×0.5```
- Total: ×1 (porque 2 * 0.5 = 1)!

Abaixo, há a matriz de tipos:
![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Pokemon_Type_Chart.svg/1024px-Pokemon_Type_Chart.svg.png)

Vocês podem construir uma função de "vantagem de tipo" entre dois Pokémon com base em seus tipos, usando a PokeAPI ou uma tabela estática como dicionário.
```python
def get_effectiveness(attacker_type, defender_type):
    effectiveness = {
        "fire": {"grass": 2.0, "water": 0.5, "fire": 0.5},
        "water": {"fire": 2.0, "grass": 0.5, "water": 0.5},
        "grass": {"water": 2.0, "fire": 0.5, "grass": 0.5}
    }
    return effectiveness.get(attacker_type, {}).get(defender_type, 1.0) # É pra sempre retornar 1 indicando Normalmente eficaz!

```

## Arquitetura geral da solução
Cada Pokémon passa por uma mesma CNN para extrair seu embedding vetorial (ex: 128D). Utiliza-se alguma regra interna de combinação das informações e a MLP classifica o resultado (vitória, empate, derrota).

**Entradas:**

- Duas **imagens** de Pokémon (ex: `pikachu.png`, `charizard.png`).
- (Opcional) Seus **tipos e atributos** podem ser utilizados no pré-processamento para gerar os rótulos.

**Rotulação (Sugestão):**
Exemplo de rótulo com base em tipo e poder ofensivo:

```python
def duel_result(p1, p2):
    advantage = type_advantage(p1['type'], p2['type'])  # +1, 0 ou -1
    power_diff = (p1['attack'] + p1['special-attack']) - (p2['attack'] + p2['special-attack'])

    if advantage + np.sign(power_diff) >= 1:
        return 2  # p1 vence
    elif advantage + np.sign(power_diff) <= -1:
        return 0  # p1 perde
    else:
        return 1  # empate

```

**Saída:**

- Uma **classe categórica**:
  - `0`: 1º Pokémon perde
  - `1`: empate
  - `2`: 1º Pokémon vence

**Modelo fake:**
```python
# Entrada: img1, img2
embed1 = CNN(img1)
embed2 = CNN(img2)

x = concat([embed1, embed2, abs(embed1 - embed2)])
output = Dense(3, activation='softmax')(MLP(x))
```
## Avaliação

Bolei uma forma SUBJETIVAS de avaliar o resultado por Coerência Semântica, isto é, se a previsão do modelo parece plausível dentro do universo Pokémon;

**Tabela de Casos para Avaliação Subjetiva**

| Nº   | Pokémon 1                     | Tipo(s) 1     | Pokémon 2     | Tipo(s) 2       | Expectativa "Lógica Pokémon"  | Categoria | Justificativa                                            |
| ---- | ----------------------------- | ------------- | ------------- | --------------- | ----------------------------- | --------- | -------------------------------------------------------- |
| 1    | **Pikachu**  ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png)                 | Elétrico      | **Gyarados** ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/130.png) | Água/Voador     | Pikachu vence                 | Clássico  | Elétrico é 4x eficaz contra Água/Voador                  |
| 2    | **Charizard** ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png)                | Fogo/Voador   | **Blastoise** ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png) | Água            | Charizard perde               | Clássico  | Água é forte contra Fogo                                 |
| 3    | **Venusaur**  ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png)                | Planta/Veneno | **Charizard** ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png)  | Fogo/Voador     | Venusaur perde                | Clássico  | Fogo é forte contra Planta                               |
| 4    | **Machamp**   ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/68.png)                | Lutador       | **Alakazam** ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png) | Psíquico        | Machamp perde                 | Clássico  | Psíquico é forte contra Lutador                          |
| 5    | **Golem** ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/76.png)                    | Pedra/Terra   | **Blastoise** ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png) | Água            | Golem perde                   | Clássico  | Água é forte contra Terra/Pedra                          |
| 6    | **Scyther**  ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/123.png)                  | Inseto/Voador | **Charizard** ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png) | Fogo/Voador      | Scyther perde                 | Clássico  | Fogo é forte contra Inseto                               |
| 7    | **Jigglypuff** ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png)                | Normal/Fada   | **Gengar** ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png)    | Fantasma/Veneno | Jigglypuff perde              | Clássico  | Fantasma imune a Normal, forte contra Fada               |
| 8    | **Electabuzz**   ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/125.png)               | Elétrico      | **Rhydon** ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/112.png)     | Terra/Pedra     | Electabuzz perde (sem efeito) | Clássico  | Elétrico não afeta tipo Terra                            |
| 9    | **Magikarp**     ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/129.png)               | Água          | **Machamp** ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/68.png)   | Lutador         | Magikarp perde                | Absurdo   | Magikarp é notoriamente fraco                            |
| 10   | **Caterpie**  ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/10.png)                 | Inseto        | **Arcanine** ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/59.png)    | Fogo            | Caterpie perde                | Absurdo   | Inseto fraco contra Fogo, Caterpie tem stats baixíssimos |
| 11   | **Farfetch’d**   ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/83.png)             | Normal/Voador | **Zapdos** ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/145.png)    | Elétrico/Voador | Farfetch’d perde              | Absurdo   | Diferença massiva de stats e fama                        |
| 12   | **Ditto** (sem transformação) ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png) | Normal        | **Dragonite** ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/149.png) | Dragão/Voador   | Ditto perde (na prática)      | Absurdo   | Ditto precisa de transformação para lutar bem            |
| 13   | **Metapod** ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/11.png)                  | Inseto        | **Charizard** ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png)   | Fogo/Voador     | Metapod perde                 | Absurdo   | Metapod só usa Harden, fraco vs Fogo                     |
| 14   | **Snorlax**   ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/143.png)                | Normal        | **Hitmonlee** ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/106.png) | Lutador         | Snorlax perde                 | Clássico  | Lutador é eficaz contra Normal                           |
| 15   | **Dragonite** ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/149.png)                | Dragão/Voador | **Articuno** ![](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/144.png)  | Gelo/Voador     | Dragonite perde               | Clássico  | Gelo é 4x eficaz contra Dragão/Voador                    |


## Regras gerais

A seguir, as regras que delimitam os aspectos desse projeto:

- Utilizem os dados da segunda geração em diante, do 152º ao 1015º, para treino e os da primeira geração, do 1º ao 151º, para teste;
- Não pode usar rede treinada, ou seja, o treinamento tem que partir de vocês;
- Não pode fazer aprendizagem por transferência;
- Não pode pré-processar a imagem, com exceção de transformações de escala dos pixels ou redimensionamento da entrada;
- O treinamento tem de ser via Google Colab.
 
