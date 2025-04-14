

[![logo](ppgc_logo.png)](https://ppgcc.ifce.edu.br/)

---

# DEEP101 - Aprendizagem Profunda (2025)

Conhecer os conceitos fundamentais de aprendizado profundo, permitindo que os discentes possuam conhecimentos necessários para o aprofundamento em qualquer campo da área e que possam desenvolver métodos, ferramentas e aplicações inteligentes.

[Clique aqui e baixe o Programa de Unidade Didática da disciplina.](suplementar/pud-aprendizagem-profunda.pdf)

## Professores
Prof. Dr. Saulo Oliveira [Lattes](http://lattes.cnpq.br/9883694006602467) | [Google Scholar](https://scholar.google.com.br/citations?user=rRTkRcAAAAAJ) | [ORCID](http://orcid.org/0000-0001-6362-6113)

e-mail: saulo.oliveira@ifce.edu.br

## Informações
**Horário**: Às terças, das 13:00 às 15:00.

**Local**: Sala 204, Bloco de Pós-graduação. Instituto Federal de Educação, Ciência e Tecnologia do Ceará | *campus* Fortaleza.

**Endereço**: Avenida Treze de Maio, nº 2081 - Benfica - CEP: 60040-215 - Fortaleza/CE.

## Pré-requisitos
Apesar das disciplinas do PPGCC não exigirem ```pré-requisitos```, o conhecimento das seguintes ferramentas será de grande valia para acelarar a curva de aprendizado durante a disciplina.

| 🐍  Python (Numpy & PyTorch)                                  | 🔢  Álgebra Linear                                            | 🧮 Cálculo (Derivadas)                                        |
| :----------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Todas as atividades serão em Python e usaremos o formato de Notebooks do Jupyter para entrega. | Usaremos transposição de matriz, inversa e operações algébricas com expressões de matrizes. | Você precisará obter uma derivada e maximizar uma função descobrindo onde a derivada = 0. |

## Como vai ser a nota?
A avaliação da disciplina é qualitativa e visa o caminho da aprendizagem. Assim, ao invés de um valor número na escala 0-10, uma letra é atribuída. Esta letra indica um conjunto de fatores que são observados ao se realiazar as atividades avaialiativas durante a disciplina. A seguir, nos cards abaixo, são listados os fatores observados e a letra associada a cada um deles.

| A                                                            | B                                                            | C                                                            | D                                                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| $\bullet$ Compreendeu por completo a proposta da atividade;<br/>$\bullet$ O trabalho está ótimo e completo;<br/>$\bullet$ O discente está pronto para o próximo assunto. | $\bullet$ Compreendeu a maior parte da proposta da atividade;<br/>$\bullet$ O trabalho está bom e completo;<br/>$\bullet$ O discente tem condições de progredir. | $\bullet$ Compreendeu parte da proposta da atividade;<br/>$\bullet$ O trabalho está incompleto;<br/>$\bullet$ O discente precisa de auxílio para compreender o assunto. | $\bullet$ Não compreendeu por completo a proposta da atividade;<br/>$\bullet$ O trabalho precisa ser refeito;<br/>$\bullet$ O discente não tem condições objetivas de progredir. |

Além do resultado da avaliação qualitativa, cada atividade avaliativa possui um peso associado. Em posse de cada avaliação e seu respectivo peso, a nota final que é a que vai para o histórico é calculada conforme a seguinte fórmula:

$$\text{Nota final} = \dfrac{\sum\limits^N_{i} a_i * w_i }{\sum\limits^N_{i} a_i} \text{ em que } a_i=\begin{cases}
    4, & \text{se } a_i = A;\\
    3, & \text{se } a_i = B;\\
    2, & \text{se } a_i = C;\\
    1, & \text{se } a_i = D;\\
    0, & \text{se não entregue.}
\end{cases},$$

em que $N$ representa o número de atividades na disciplina. 

Observe um caso ilustrativo -- o número entre parênteses representa o peso da atividade:

|          | Prova (2) | Simulação (1) | Relatório (1) | Seminário (1) | Nota final |
| -------- | :-------: | :-----------: | :-----------: | :-----------: | :--------: |
| Huguinho |     A     |       A       |       B       |       A       |    9,5     |
| Zezinho  |     B     |       B       |       B       |       C       |    7,0     |
| Luizinho |     C     |       A       |       B       |       B       |    8,0     |
| Donald   |     B     |       D       |       C       |       C       |    4,5     |

## Cronograma e Conteúdo Programático

> Este é o plano de estudos da turma de 2025 do curso (ainda em construção).

| Tipo      | Data       | Descrição                                               | Material                                                     |
| --------- | ---------- | ------------------------------------------------------- | ------------------------------------------------------------ |
| Aula      | 15/04/2025 | Introdução à Aprendizagem de máquina                    | [Slides](slides/dl_01_ml.pdf)  • [Atividade](atividades/resumo_pedrod.md) • [Artigo do Pedro Domingos](https://dl.acm.org/doi/pdf/10.1145/2347736.2347755) |
| Aula      | 22/04/2025 | Perceptron  & Adaline                                            | [Slide Perceptron](slides/dl_02_perceptron.pdf) • [Slide Adaline](slides/dl_03_adaline.pdf) • [Atividade classificação Salmão *vs.* Robalo](atividades/perceptron-salmao-robalo.md) |
| Aula      | 29/04/2025 | Perceptron multicamadas (MLP) & Redes de treino rápido                                                 | [Slide MLP](slides/dl_04_mlp.pdf) • [Slide RBF & ELM](slides/dl_07_treino_rapido.pdf) • [Atividade Datasets 2D](atividades/mlp_2d.md) |
| Aula      | 06/05/2025 | Normalização & Otimizadores                           | [Slide Normalização](slides/dl_05_normalizacao.pdf) • [Slide Otimizadores (seção só)](slides/dl_08_introdl.pdf) • [Notebook PyTorch](suplementar/Intro_ao_PyTorch.ipynb) •  [Atividade](#) |
| Aula      | 13/05/2025 | Seleção de Modelos e Projeto de Experimentos                                            | [Slides](#) • [Atividade ](#) |
| Prova     | 20/05/2025 | Perceptron, Adaline e MLPs                              | [Prova (RNA) 2022](suplementar/2022_rna_exam.pdf)  •  [Prova (DL) 2023](suplementar/2023_rna_exam.pdf)  •  [Prova (DL) 2024](suplementar/2024_dl_exam.pdf) |
| Aula | 27/05/2025 | Redes convolucionais                                    | [Slides](slides/dl_08_introdl.pdf) •                    [Desafio XXXXX](#) |
| Aula      | 03/06/2025 | Redes convolucionais famosinhas                                    | [Slides](slides/dl_06_problemas.pdf)  |
| Aula      | 10/06/2025 | Problemas comuns                         | [Slides](slides/dl_06_problemas.pdf) |
| Seminário | 17/06/2025 | Desafio CNN                                            | [Modelo Slide](https://docs.google.com/presentation/d/1CaxWihoUNVIszqsCwFethmMr-lcYoGO_L456NH5TOZ0/edit?usp=sharing)  |
| Aula | 24/06/2025 | Resumo de Teoria da Probabilidade | [Slides](slides/dl_16_probabilidade-completa.pdf)  • [Atividade](atividades/#)  |
| Aula      | 22/07/2025 | Redes autocodificadoras e Redes adversárias generativas | [Slides](slides/dl_10_ae_vae_gan.pdf) • [Atividade ](#) |
| Aula      | 29/07/2025 | Redes recorrentes                                       | [Slides](slides/dl_11_recorrent.pdf) • [Atividade ](#) |
| Prova     | 05/08/2025 | Solução de problemas da indústria                       | Nenhum.                                                      |
| Seminário | --/--/2025 | Desafio RNN/GAN/VAE - Parte 01                          | Nenhum.                                                     |
| Seminário | --/--/2025 | Desafio RNN/GAN/VAE - Parte 02                          | Nenhum.                                                |
| Seminário | --/--/2025 | Artigo final                                            | Nenhum.                                           |
| Seminário | --/--/2025 | Socialização do artigo final                            | Nenhum.                                           |

<small>Cronograma básico. Ele pode ser alterado a qualquer momento por eventos diversos.</small>

## Diretrizes da Sessão de Pôsteres

O objetivo de um pôster é dar ao espectador um resumo rápido do trabalho, que não apenas atrai seu interesse, mas também o motiva a aprender mais sobre o projeto. Para uma introdução à criação de pôsteres acadêmicos, consulte [Guia de postêres](https://guides.nyu.edu/posters) da Universidade de Nova Iorque. Aqui está um exemplo de estrutura que pode ser útil:

| Problema                                                     | Antecedentes                                                 | Métodos                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| O que você está tentando resolver? Consulte os desafios atuais e por que seu trabalho é significativo. | Configuração do problema + notação; talvez trabalhos anteriores. | Explique suas contribuições técnicas; números podem realmente ajudar a entender especialmente para um modelo neural! |

| Experimentos                                                 | Análise                                                      | Conclusão e referências                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Qual é a tarefa? Quais são as entradas e saídas do modelo? O que são as resultados? Compare com as linhas de base; para resultados, um gráfico pode dizer muito mais do que uma tabela do mesmo tamanho! | Forneça uma análise aprofundada de certos casos de interesse ou contextualize seus resultados na literatura existente! Adicione alguns gráficos/exemplos/visualizações. | Tire brevemente algumas conclusões do trabalho.<br/>Se o espaço permitir, considere adicionar 1-3 referências muito importantes (não faça mais do que isso!) |

