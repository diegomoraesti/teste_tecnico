# Coleta de Partidas do Brasileirão Série A - API

  

Este projeto coleta os jogos da próxima rodada do **Brasileirão Série A** diretamente do API **ESPN**, trata os dados de data e hora para o fuso horário de Brasília e exporta os resultados para CSV.



---

  

## Autor

  

- **Diego Moraes Leal**  

- Data de criação: 21/10/2025

  

---

## Instalação:

- Realizar download da versão do python(https://www.python.org/downloads/).

- Instalar dependência através do comando: "pip install -r requirements.txt" , que deve ser executado sem as aspas diretamente no terminal, após a instalação do python.
  

## Funcionalidades

  

- Acessa o API da ESPN, no link https://site.api.espn.com/apis/site/v2/sports/soccer/bra.1/scoreboard

- Coleta os jogos da próxima rodada do Brasileirão Série A da API.  

- Realiza tratamento de data e hora.

- Seleciona os próximos jogos disponíveis na tabela.

- Formata as informações, adicionando cabeçalho e selecionando informações necessárias

- Permite geração de arquivo .csv

  

## Arquitetura

  

O projeto consiste na obtenção de dados de uma tabela especifica não havendo necessidade de desenvolvimento complexo por isso optei Clean Code

  

- Funções pequenas e claras (cada função faz apenas uma coisa).

- Nomes autoexplicativos (variáveis, funções e classes).

- Separação de responsabilidades (coleta, tratamento, exportação).

- Evitar “hardcode” espalhado pelo código.

- Documentação e comentários claros.

## Dependências

  

Certifique-se de ter as seguintes bibliotecas instaladas:

  

```bash

pip install pandas