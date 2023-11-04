# Data extraction from PDF files with pdfplumber

## What is pdfplumber

[pdfplumber](https://pypi.org/project/pdfplumber/0.1.2/) is a Python library created for data extraction from PDF files. 

## Description

The [Annual Budget Execution Report (RREO)](https://www.tesourotransparente.gov.br/temas/contabilidade-e-custos/relatorio-resumido-da-execucao-orcamentaria-rreo-uniao#:~:text=O%20Relat%C3%B3rio%20Resumido%20da%20Execu%C3%A7%C3%A3o,da%20receita%20e%20da%20despesa.) is a publication of fiscal data for each Brazilian state or municipality. It has multiple annexes that you can extract data from [API](https://apidatalake.tesouro.gov.br/docs/siconfi/#/). But, unfortunetly, one of the annexes is available only in PDF format. In this case, I've decided to extract data using pdfplumber. [Here](https://www.fnde.gov.br/siope/relatoriosEstaduais.jsp) it's possible to download all the PDF files for each state or municipality.





