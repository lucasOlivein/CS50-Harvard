# Cyberchase

## Descrição do Problema

Neste problema, é fornecido um banco de dados chamado `cyberchase.db`, que contém informações sobre episódios da série *Cyberchase*, exibida pela PBS. O banco de dados inclui uma única tabela chamada `episodes`, e o objetivo é escrever consultas SQL que respondam a uma série de perguntas com base nos dados fornecidos.

## Especificação

- Cada consulta deve consistir em uma única instrução `SELECT`.
- Nenhuma suposição deve ser feita sobre os valores da coluna `id` — as consultas devem permanecer válidas independentemente desses valores.
- Cada consulta deve retornar **apenas** os dados necessários para responder à pergunta — por exemplo, se for solicitado o título dos episódios, outras informações como datas de exibição não devem ser incluídas no resultado.

## Conjunto de Dados

Para este problema, são fornecidos o banco de dados `cyberchase.db` e *treze* arquivos `.sql` vazios.  
A tabela `episodes`, presente em `cyberchase.db`, possui as seguintes colunas:

- `id`: identifica de forma única uma linha da tabela.
- `season`: número da temporada em que o episódio foi exibido.
- `episode_in_season`: número do episódio dentro da temporada.
- `title`: título do episódio.
- `topic`: tema abordado pelo episódio.
- `air_date`: data (AAAA-MM-DD) em que o episódio foi ao ar.
- `product_code`: código único usado internamente pela PBS para identificar cada episódio.

## Questões

Abaixo está a lista das 13 perguntas a serem respondidas utilizando consultas SQL.  
Cada consulta deve ser escrita em um arquivo separado, nomeado de acordo com o número da questão (por exemplo, `1.sql` para a questão 1, `2.sql` para a questão 2, e assim por diante).

- [X] **Q1:** Listar os títulos de todos os episódios da Temporada 1.
- [X] **Q2:** Listar o número da temporada e o título do primeiro episódio de cada temporada.
- [X] **Q3:** Encontrar o código de produção do episódio intitulado “Hackerized!”.
- [X] **Q4:** Encontrar os títulos dos episódios que não possuem um tema listado.
- [X] **Q5:** Encontrar o título do episódio especial de feriado exibido em 31 de dezembro de 2004.
- [X] **Q6:** Listar os títulos dos episódios da Temporada 6 (2008) que foram lançados antecipadamente, em 2007.
- [X] **Q7:** Listar os títulos e os temas de todos os episódios que ensinam frações.
- [X] **Q8:** Contar quantos episódios foram lançados entre 2018 e 2023 (inclusive).
- [X] **Q9:** Contar quantos episódios foram lançados nos seis primeiros anos de Cyberchase (2002–2007, inclusive).
- [X] **Q10:** Listar os IDs, títulos e códigos de produção de todos os episódios, ordenados pelo código de produção (do mais antigo ao mais recente).
- [X] **Q11:** Listar os títulos dos episódios da Temporada 5, em ordem alfabética reversa.
- [X] **Q12:** Contar quantos títulos de episódios são únicos.
- [X] **Q13:** Escrever uma consulta à escolha que contenha pelo menos uma condição utilizando `WHERE` com `AND` ou `OR`.

## Dicas Fornecidas

- O operador `BETWEEN` pode ser usado com datas, por exemplo:

  ```sql
  WHERE air_date BETWEEN '2000-01-01' AND '2000-12-31'
  ```

## Fonte
Este README foi baseado na documentação do problema Cyberchase do curso CS50’s Introduction to Databases with SQL, da Universidade de Harvard, disponível em: [https://cs50.harvard.edu/sql/2023/problems/0/cyberchase](https://cs50.harvard.edu/sql/2023/problems/0/cyberchase)