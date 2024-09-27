# Fórmula E - Site Interativo e Gamificado

# Equipe Ares
Popularização da Fórmula E
### Descrição
Este projeto visa popularizar a Fórmula E através de um site interativo e gamificado, que apresenta informações detalhadas sobre as corridas, circuitos, estatísticas, classificações, carros e oferece passeios virtuais.

# Integrantes
- RM 558638 - Gabriel Guilherme Leste
- RM 555798 - Glauco Heitor Gonçalves
- RM 556452 - Otávio Santos Lima
- RM 554787 - Victor Hugo de Paula


Este repositório contém um script em Python para suportar funcionalidades interativas e gamificadas relacionadas ao site da Fórmula E.

## Estruturas de Programação Implementadas

### Entrada, Processamento e Saída de Dados

- Utilização de f-strings para formatação de strings.
- Manipulação de dados utilizando variáveis, listas, dicionários e outros tipos de dados conforme necessário.

### Estruturas Condicionais e de Repetição

- Utilização de `if`, `elif`, `else`, `for` e `while` para controle de fluxo conforme necessário.

### Funções

- Definição de funções com passagem de parâmetros e retorno de valores para modularização do código.

### Manipulação de Arquivos

- Leitura e escrita de arquivos utilizando a biblioteca padrão do Python (`csv` para manipulação de CSV).

### Bibliotecas Externas

- Utilização de bibliotecas como `pandas` para manipulação de dados tabulares e `matplotlib` para visualização de dados.

## Funcionalidades Implementadas

### saudacao(nome)

- Função que recebe um nome como parâmetro e retorna uma saudação personalizada, utilizando f-string para interpolação de string. Inclui links para informações detalhadas sobre circuitos, carros e passeios virtuais.

### carregar_dados(caminho_arquivo)

- Função que carrega dados de um arquivo CSV e retorna uma lista de dicionários representando os dados.

### exibir_estatisticas(df)

- Função que recebe um DataFrame do pandas como parâmetro e exibe estatísticas básicas utilizando o método `describe()`.

### exibir_classificacoes(df)

- Função que recebe um DataFrame como parâmetro, agrupa os dados pela coluna 'piloto' e exibe as classificações dos pilotos de acordo com a soma de pontos, em ordem decrescente.

### visualizar_dados(df)

- Função que recebe um DataFrame como parâmetro e cria um gráfico de barras mostrando a soma de pontos por ano, utilizando o método `plot(kind='bar')` do pandas e matplotlib para visualização.

### Por fim, o código chama a função executar_programa() para iniciar a execução do programa

- Função principal que inicia o programa, solicitando o nome do usuário e o caminho do arquivo CSV. Carrega os dados, exibe estatísticas, classificações e visualiza os dados em caso de sucesso. Captura e exibe mensagens de erro caso ocorra alguma exceção durante a execução.

## Uso

Para executar o programa:
1. Clone este repositório.
2. Execute o script Python `sprint1.py`.
3. Siga as instruções fornecidas para interagir com as funcionalidades do programa.
4. Exemplo do resultado final
   ![Captura de tela 2024-06-17 150436](https://github.com/OTAVIO48FERRAO/sprint1-python/assets/165107024/fe066c84-a137-4c8b-9ba0-58ea93d8189b)

Este script é projetado para fornecer uma experiência interativa e informativa relacionada às corridas da Fórmula E, abrangendo desde a saudação inicial até a visualização de estatísticas e gráficos de desempenho das equipes e pilotos.

