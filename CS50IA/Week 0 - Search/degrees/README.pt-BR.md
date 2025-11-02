Este README também está disponível em [inglês](README.md).

# Graus

De acordo com o jogo *Six Degrees of Kevin Bacon*, qualquer pessoa da indústria cinematográfica de Hollywood pode ser conectada a Kevin Bacon em até seis passos, onde cada passo consiste em encontrar um filme em que dois atores atuaram juntos.

## Descrição do Problema

Neste problema, o objetivo é encontrar o caminho mais curto entre dois atores, escolhendo uma sequência de filmes que os conecte. Por exemplo, o caminho mais curto entre Jennifer Lawrence e Tom Hanks é 2: Jennifer Lawrence está conectada a Kevin Bacon por ambos atuarem em *X-Men: First Class*, e Kevin Bacon está conectado a Tom Hanks por ambos atuarem em *Apollo 13*.

Esse problema pode ser modelado como um problema de busca:

- Os **estados** são pessoas.  
- As **ações** são filmes, que nos levam de um ator a outro (é verdade que um filme pode nos levar a vários atores, mas isso é aceitável para este problema).  
- O **estado inicial** e o **estado final** são definidos pelas duas pessoas que estamos tentando conectar.  

Usando a **busca em largura (breadth-first search)**, conseguimos encontrar o caminho mais curto entre dois atores.

## Visão Geral do Conjunto de Dados

O código fornecido vem com dois conjuntos de arquivos CSV: os diretórios `large` e `small`. Ambos contêm arquivos com os mesmos nomes e a mesma estrutura, mas `small` é um conjunto reduzido, útil para testes e experimentações rápidas.

Cada conjunto inclui três arquivos CSV:
- `people.csv`: Cada pessoa possui um `id` único, um `name` e um `birth year`.
- `movies.csv`: Cada filme possui um `id`, um `title` e um `year`.
- `stars.csv`: Cada linha vincula um `person_id` a um `movie_id`.

## Visão Geral do Código

Agora, ao analisar o arquivo `degrees.py`. No início do arquivo, várias estruturas de dados são definidas para armazenar informações dos arquivos CSV:
- `names`: mapeia nomes para um conjunto de IDs  
- `people`: mapeia o ID de cada pessoa para um dicionário com suas informações  
- `movies`: mapeia os IDs dos filmes para informações e elenco  

A função `load_data` carrega os dados dos arquivos CSV nessas estruturas.

A função `main` primeiro carrega os dados na memória (o diretório de onde os dados são carregados pode ser especificado via argumento na linha de comando). Em seguida, o programa solicita ao usuário que digite dois nomes.

A função `person_id_for_name` resolve esses nomes recuperando o ID correspondente a cada pessoa (e também lida com casos em que há mais de uma pessoa com o mesmo nome, solicitando esclarecimento ao usuário).

Depois que os dois IDs são encontrados, a função `shortest_path` é chamada para calcular a menor conexão entre eles, usando os vínculos de filmes. O resultado é então impresso como uma sequência de passos.

No entanto, a função `shortest_path` ainda não foi implementada. É aí que você entra!

## Especificação

Implemente a função `shortest_path(source, target)` de forma que ela retorne o caminho mais curto entre os IDs `source` e `target`.

- Supondo que exista um caminho entre `source` e `target`, a função deve retornar uma lista onde cada item representa o próximo par `(movie_id, person_id)` no caminho. Cada par deve ser uma tupla de duas strings.
    - Por exemplo, se o retorno da função for `[(1, 2), (3, 4)]`, isso significa:
        - `source` atuou no filme `1` com a pessoa `2`  
        - A pessoa `2` atuou no filme `3` com a pessoa `4`  
        - A pessoa `4` é o destino (`target`)  

- Se houver múltiplos caminhos de menor comprimento, sua função pode retornar qualquer um deles.
- Se não existir um caminho possível entre os dois atores, sua função deve retornar `None`.

Você pode utilizar a função `neighbors_for_person(person_id)`, que retorna um conjunto de pares `(movie_id, person_id)` representando todas as pessoas que atuaram em um filme com a pessoa informada.

## Dicas
- Embora a implementação da busca em largura na aula verifique o objetivo quando um nó é retirado da fronteira, você pode melhorar a eficiência verificando se é o objetivo no momento em que os nós são adicionados à fronteira. Se detectar um nó objetivo, não há necessidade de adicioná-lo à fronteira — basta retornar a solução imediatamente.

Você pode aproveitar e adaptar qualquer código dos exemplos da aula. Já fornecemos um arquivo `util.py` que contém as implementações da aula para `Node`, `StackFrontier` e `QueueFrontier`, que você pode usar (e modificar, se quiser).

## Fonte
Este README foi baseado na documentação do projeto *Degrees* do curso de Inteligência Artificial da Harvard, disponível em: [https://cs50.harvard.edu/ai/2024/projects/0/degrees/](https://cs50.harvard.edu/ai/2024/projects/0/degrees/).
