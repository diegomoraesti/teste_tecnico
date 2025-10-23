# Coleta de Partidas do Brasileirão Série A - GE

Este projeto coleta os jogos da próxima rodada do **Brasileirão Série A** diretamente do site do **GE (Globo Esporte)**, trata os dados de data e hora para o fuso horário de Brasília e exporta os resultados para CSV.

---

## Autor

- **Diego Moraes Leal**  
- Data de criação: 21/10/2025

---
## Instalação:
- Realizar download da versão do python(https://www.python.org/downloads/).
- Instalar dependência através do comando: "pip install -r requirements.txt" , que deve ser executado sem as aspas diretamente no terminal, após a instalação do python.
- Após a instalação da dependencia, executar o comando: "playwright install", também no terminal e sem aspas, este comando irá instalar os navegadores necessários à funcionalidade do sistema.

## Funcionalidades

- Acessa o site da globo, parte de esportes.
- Coleta os jogos da próxima rodada do Brasileirão Série A do site GE.  
- Realiza tratamento de data e hora.
- Seleciona os próximos jogos disponíveis na tabela.
- Formata as informações, adicionando cabeçalho e selecionando informações necessárias 
- Permite geração de arquivo .csv e .xlsx

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
pip install pandas playwright pytz