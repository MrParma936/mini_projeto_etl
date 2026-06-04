# Mini Projeto ETL com Python

## Descrição

Este projeto tem como objetivo aplicar conceitos de ETL (Extract, Transform and Load) utilizando Python puro para realizar a leitura, limpeza, transformação e análise de dados provenientes de datasets da Olist.

Durante o desenvolvimento foram utilizadas estruturas nativas da linguagem Python, como variáveis, listas, dicionários, estruturas condicionais, laços de repetição, funções e bibliotecas nativas como csv, re e datetime, sem uso de bibliotecas de análise de dados como Pandas.

---

## Contextualização

A equipe de Engenharia de Dados da Olist extraiu lotes de dados do banco oficial em arquivos estruturados (olist_products_dataset.csv e olist_orders_dataset.csv), mas identificou inconsistências que estão travando os relatórios automatizados.
Dessa forma faz-se necessário que os dados passem por um processo de ETL a fim de minimizar a ocorrência de Overfiting ou Underfiting.

---

## Objetivos

* Ler os dados dos arquivos CSV.
* Identificar e tratar valores nulos.
* Normalizar informações textuais.
* Contabilizar ocorrências de categorias.
* Remover inconsistências nos dados.
* Produzir informações úteis para futuras análises e aplicações de Machine Learning.

---

## Tecnologias Utilizadas

* Python 3
* CSV (biblioteca nativa)
* Regex (biblioteca re)
* Datetime (biblioteca datetime)
* VS Code

---

## Estrutura do Projeto

```text
mini_projeto_etl/
│
├── main.py
├── funcoes.py
├── olist_products_dataset.csv
├── olist_orders_dataset.csv
└── README.md
```

---

## Funcionalidades Implementadas

### Leitura de Arquivos

* Leitura dos datasets através da biblioteca nativa csv e gerenciador de contexto with open().
* Armazenamento dos dados em variáveis com estruturas de listas e dicionários.
* Exibição em tela de alguns registros provenientes dos datasets.
* Quantificação do tamanho dos conjuntos de dados.

### Tratamento de Valores Nulos

* Identificação de registros com valores vazios.
* Contagem de ocorrências de valores nulos.
* Remoção de registros inconsistentes quando necessário.

### Normalização de Dados

* Conversão de textos para letras minúsculas.
* Remoção de espaços extras.
* Remoção de caracteres especiais utilizando Regex.
* Padronização das categorias dos produtos.

### Normalização de Formato de Datas

* Utilização da biblioteca datetime para leitura de datas.
* Conversão do formato de string original para o formato simplificado brasileiro.

### Análise Exploratória

* Contagem de categorias.
* Identificação dos valores mais frequentes.
* Ordenação dos resultados por quantidade de ocorrências.
* Análise da hipótese de negócio da Olist, em que a ocorrência de datas nulas estaria relacionada a condição de status cancelado.

---

## Resultados Obtidos

O processo de limpeza permitiu padronizar os dados e reduzir inconsistências que poderiam prejudicar análises futuras.

Após a normalização das categorias, foi possível obter contagens mais precisas e evitar que registros equivalentes fossem tratados como categorias diferentes devido a diferenças de formatação.

---

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/MrParma936/mini_projeto_etl.git
```

2. Baixe o arquivo ZIP dos datasets no repositório:

```bash
https://github.com/fiesc-junior-prado/mine_projeto_bloco_1
```

3. Entre na pasta do projeto:

```bash
cd mini_projeto_etl
```

4. Execute o arquivo principal:

```bash
python main.py
```

---

## Autor

Marcio Roberto Parma

Projeto desenvolvido como atividade prática de ETL e preparação de dados para aplicações de Inteligência Artificial e Machine Learning.

---

## Reflexão Teórica sobre Machine Learning

A etapa de limpeza e preparação dos dados é fundamental para o sucesso de qualquer modelo de Machine Learning. Quando os dados contêm valores inconsistentes, categorias duplicadas por diferenças de escrita, registros incompletos ou informações incorretas, o algoritmo pode aprender padrões errados. Por isso, a aplicação de uma lógica de programação adequada durante o processo de ETL ajuda a garantir que os dados utilizados no treinamento sejam mais representativos da realidade.

Além disso, dados mal preparados podem contribuir para problemas como overfitting e viés. O overfitting ocorre quando o modelo aprende detalhes específicos e ruídos presentes nos dados de treinamento, perdendo capacidade de generalização para novos casos. Já o viés pode surgir quando determinados grupos ou informações são representados de forma incorreta ou desigual no conjunto de dados. Dessa forma, técnicas de limpeza, normalização e validação dos dados ajudam a construir bases mais consistentes e equilibradas, aumentando a qualidade e a confiabilidade dos futuros modelos de Inteligência Artificial.
