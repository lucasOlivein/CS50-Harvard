Este README também está disponível em [inglês](README.md).

# Jogadores
## Contexto

O beisebol é um esporte amplamente popular, especialmente nos Estados Unidos e no Canadá. No jogo, dois times com nove jogadores alternam entre rebater (acertar a bola) e defender (capturar e arremessar as bolas rebatidas). Pontos — conhecidos como “corridas” — são marcados quando um jogador do time que rebate consegue acertar a bola e alcançar todas as bases com sucesso antes de ser eliminado pelo time adversário. A *Major League Baseball* (MLB), principal liga profissional do esporte, atua como a organização oficial desde 1876.

## Descrição do Problema

Neste problema, o objetivo é responder a perguntas sobre jogadores da MLB utilizando dados contidos no banco de dados `players.db`, especificamente na tabela `players`, que reúne informações sobre atletas que jogaram entre os anos de 1871 e 2023.

## Conjunto de Dados

Para este problema, são fornecidos o banco de dados `players.db` e *dez* arquivos `.sql` vazios — um arquivo adicional, o décimo primeiro, está incluído para a questão opcional.  
A única tabela `players` presente em `players.db` contém as seguintes colunas:

- `id`: identifica de forma única cada linha (jogador) na tabela.
- `first_name`: o primeiro nome do jogador.
- `last_name`: o sobrenome do jogador.
- `bats`: o lado (R para destro ou L para canhoto) com o qual o jogador rebate.
- `throws`: a mão (R para direita ou L para esquerda) com a qual o jogador arremessa.
- `weight`: o peso do jogador em libras.
- `height`: a altura do jogador em polegadas.
- `debut`: a data (no formato AAAA-MM-DD) em que o jogador iniciou sua carreira na MLB.
- `final_game`: a data (no formato AAAA-MM-DD) em que o jogador disputou sua última partida na MLB.
- `birth_year`: o ano de nascimento do jogador.
- `birth_month`: o mês de nascimento do jogador (como um número inteiro).
- `birth_day`: o dia de nascimento do jogador.
- `birth_city`: a cidade onde o jogador nasceu.
- `birth_state`: o estado onde o jogador nasceu.
- `birth_country`: o país onde o jogador nasceu.

## Especificações

- Cada consulta deve consistir em uma única instrução `SELECT`.
- Não se deve fazer suposições sobre os valores de `id` — as consultas devem continuar válidas independentemente desses valores.
- Cada consulta deve retornar **apenas** os dados necessários para responder à pergunta.
- Cada consulta SQL deve ser escrita em um arquivo separado, nomeado de acordo com o número da respectiva pergunta (por exemplo, `1.sql` para a pergunta 1, `2.sql` para a pergunta 2, e assim por diante).

## Perguntas

Abaixo está a descrição das 11 perguntas respondidas neste conjunto de exercícios.

- [X] **Q1:** Encontrar a cidade natal (incluindo cidade, estado e país) de Jackie Robinson.
- [X] **Q2:** Descobrir de que lado (ex.: direito ou esquerdo) Babe Ruth rebatia.
- [X] **Q3:** Encontrar os IDs das linhas em que o valor da coluna `debut` está ausente.
- [X] **Q4:** Encontrar os nomes e sobrenomes dos jogadores que não nasceram nos Estados Unidos. Ordenar os resultados alfabeticamente por nome, depois por sobrenome.
- [X] **Q5:** Retornar os nomes e sobrenomes de todos os jogadores destros ao rebater. Ordenar os resultados alfabeticamente por nome, depois por sobrenome.
- [X] **Q6:** Retornar o nome, sobrenome e data de estreia dos jogadores nascidos em Pittsburgh, Pensilvânia (PA). Ordenar os resultados primeiro pela data de estreia — da mais recente para a mais antiga — depois alfabeticamente por nome e sobrenome.
- [X] **Q7:** Contar o número de jogadores que rebatem (ou rebatem) com uma mão e arremessam (ou arremessavam) com a outra, ou vice-versa.
- [X] **Q8:** Encontrar a altura e o peso médios, arredondados para duas casas decimais, dos jogadores que estrearam na MLB a partir de 1º de janeiro de 2000. Retornar as colunas com os nomes “Average Height” e “Average Weight”, respectivamente.
- [X] **Q9:** Encontrar os jogadores que disputaram sua última partida na MLB em 2022. Ordenar os resultados alfabeticamente por nome e sobrenome.
- [X] **Q10:** Responder a uma pergunta de sua escolha. Esta consulta deve:
  - Utilizar `AS` para renomear uma coluna.
  - Incluir ao menos uma condição usando `WHERE`.
  - Ordenar por ao menos uma coluna usando `ORDER BY`.

**Opcional:**

- [X] **Q11:** Listar os nomes e sobrenomes de todos os jogadores com altura acima da média, ordenados do mais alto para o mais baixo, depois por nome e sobrenome.

## Fonte

Este README foi baseado na documentação do problema *Players* do curso **CS50’s Introduction to Databases with SQL** da Universidade de Harvard, disponível em:  
[https://cs50.harvard.edu/sql/2024/psets/0/players/](https://cs50.harvard.edu/sql/2024/psets/0/players/)
