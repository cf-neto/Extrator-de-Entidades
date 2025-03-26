# Extrator de Entidades - Projeto em Python

<p align="center"><i>Projeto simples para extrair pessoas e lugares de um texto usando a biblioteca spaCy.</i></p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Ativo-brightgreen" alt="Status"/>
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/spaCy-v3.1.0-yellowgreen?logo=python&logoColor=white" alt="spaCy"/>
</p>

## Sobre este projeto

Este repositório contém um código em **Python** utilizando a biblioteca **spaCy** para extrair informações sobre **pessoas** e **lugares** de um texto. O código utiliza um modelo de linguagem treinado para o português (`pt_core_news_sm`) para identificar as entidades no texto e separar as pessoas e lugares encontrados.

### Funcionalidade

1. O código lê um texto e processa as entidades nomeadas.
2. Ele extrai pessoas e lugares identificados.
3. Exibe a quantidade de pessoas e lugares encontrados, além dos próprios nomes.

---

## Como Rodar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/extrator-de-entidades.git
```

## Exemplo de Entrada e Saída

**Entrada:**
```python
texto = 'Carlos foi com Isabelle para a Europa, passaram 8 dias lá, após isso foram para Itália'
```

**Saída:**
```python
{'Pessoas': ['Carlos', 'Isabelle'], 'Lugares': ['Europa', 'Itália'], 'Qtd. de pessoas encontrados': 2, 'Qtd. de lugares encontrados': 2}

