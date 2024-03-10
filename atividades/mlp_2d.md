


![logo](../ppgc_logo.png)

---

Aprendizagem Profunda – 2024.1

**Prof. Dr. Saulo Oliveira**

Data de Entrega: Uma semana após a definição.

Meio de Entrega: ```Colab com simulações```.

---

## PARTE A. Rede Perceptron de Múltiplas Camadas

1. Baixe a versão do conjunto de dados Two Moons (Tem código abaixo).
   
2. Divida de forma aleatória o conjunto entre treino (80%) e teste (20%).
   
   -  Normalize os dados com a estratégia média e desvio padrão somente pelos
dados de treino.
   
   - Treine uma rede MLP com duas camada ocultas, com até cinco neurônios cada.
   
   - Plote a superfície de decisão da MLP, adaptando o script em anexo.
   
   - Mostre a Matriz de Confusão.

1. Repita os passos anteriores para as bases de dados Ripley e Banana, também disponíveis no Google Sala de Aula.


## Exemplo de uso

```python
# Baixem do meu github
!mkdir -p local_datasets
!wget --quiet 'https://raw.githubusercontent.com/sauloafoliveira/cclw-mlm/master/local_datasets/__init__.py' -O 'local_datasets/__init__.py'
!wget --quiet 'https://raw.githubusercontent.com/sauloafoliveira/cclw-mlm/master/local_datasets/datasets-7627-10826-banana.csv' -O 'local_datasets/datasets-7627-10826-banana.csv'
!wget --quiet 'https://raw.githubusercontent.com/sauloafoliveira/cclw-mlm/master/local_datasets/rip.csv' -O 'local_datasets/rip.csv'


# importem o código assim
from local_datasets import load_banana, load_ripley, load_two_moon

bunch = load_ripley()
X, y = bunch.data, bunch.target
print(X.shape, y.shape)
```