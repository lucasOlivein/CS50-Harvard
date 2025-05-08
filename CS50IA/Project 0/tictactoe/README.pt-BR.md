Este README também está disponível em [inglês](README.md).

# Jogo da Velha (Tic-Tac-Toe)
## Objetivo 
Usar o algoritmo **Minimax** para implemenar uma IA que jogue o *Jogo da Velha* de forma ideal.

## Visão Geral do Projeto  
Este projeto consiste em dois arquivos principais: `runner.py` e `tictactoe.py`.

### Interface Gráfica: `runner.py`  
Este arquivo foi fornecido totalmente implementado. Ele cuida da interface gráfica que permite jogar visualmente.  
Concluido a lógica em `tictactoe.py`, o jogo pode ser executado com:
```python
python runner.py
```
### Lógica do Jogo: `tictactoe.py`  
Este arquivo contém a lógica principal do jogo, incluindo validação de jogadas, controle de turnos, avaliação do estado do jogo e escolha da jogada ideal.  
A maioria das funções neste arquivo foram deixadas para serem implementadas.

## Configuração Inicial

### Constantes  
No início de `tictactoe.py` são definidas três constantes:

- `X`: representa o jogador X  
- `O`: representa o jogador O  
- `EMPTY`: representa uma célula vazia no tabuleiro  

Esses valores representam o estado de cada célula do tabuleiro.

### Representação do Tabuleiro  
O tabuleiro é representado como uma lista de três listas (ou seja, uma grade 3x3).  
Cada lista interna corresponde a uma linha do tabuleiro e contém três valores: `X`, `O` ou `EMPTY`.

Por exemplo:
```python
[
    [X, O, EMPTY],  
    [EMPTY, X, EMPTY],  
    [O, EMPTY, X]  
]
```
A função `initial_state` retorna o estado inicial do tabuleiro: uma grade 3x3 onde todas as células estão como `EMPTY`.

## Especificação  
As seguintes funções em `tictactoe.py` foram deixadas para serem implementadas:

`player(board)`  
- Retorna de quem é a vez (`X` ou `O`) no tabuleiro `board`.  
- Se o tabuleiro `board` for um **tabuleiro inicial**, `X` faz a primeira jogada.  
- Os jogadores se alternam a cada jogada.  
- Se o tabuleiro `board` for um **tabuleiro terminal**, qualquer valor de retorno é aceitável (ou seja, o jogo já acabou).

`actions(board)`  
- Retorna um conjunto com todas as possíveis ações (jogadas) que podem ser feitas no tabuleiro.  
- Cada ação deve ser representada como uma tupla (i, j), onde:  
  - `i` corresponde à linha da jogada (0, 1 ou 2)  
  - `j` corresponde à coluna da jogada (0, 1 ou 2)  
- Somente células `EMPTY` são válidas.  
- Se o tabuleiro `board` for um **tabuleiro terminal**, qualquer valor de retorno é aceitável.

`result(board, action)`  
- Deve retornar um **novo tabuleiro**, sem modificar o tabuleiro `board`.  
  - O *novo tabuleiro* deve ser o tabuleiro `board` com a jogada do jogador da vez (`X` ou `O`) aplicada na coordenada `action`.  
- Se `action` não for uma coordenada válida, a função deve lançar uma exceção.

`winner(board)`  
- Retorna o vencedor (`X` ou `O`) do tabuleiro `board`, se houver um, ou `None` caso contrário.  
- Um jogador vence com três jogadas consecutivas em linha, coluna ou diagonal.

`terminal(board)`  
- Retorna `True` se o jogo acabou, ou `False` caso contrário.

`utility(board)`  
- Recebe o **tabuleiro terminal** `board` e retorna sua a pontuação:  
  - `1` se o jogador `X` venceu,  
  - `-1` se o jogador `O` venceu,  
  - `0` se houve empate.

`minimax(board)`  
- Retorna a jogada ideal (coordenada `action`) para o jogador da vez no tabuleiro `board`.  
- A jogada retornada deve ser uma ação ótima `(i, j)` válida para `board`.  
- Se houver múltiplas jogadas igualmente ótimas, qualquer uma delas pode ser retornada.  
- Se o tabuleiro `board` for um **tabuleiro terminal**, a função `minimax` deve retornar `None`.

### Suposições  
- A função `utility` só será chamada em um tabuleiro `board` se `terminal(board)` retornar `True`.  
- Haverá no máximo um vencedor (nunca ambos).  
- Para todas as funções que recebem um `board` como entrada, assume-se que o tabuleiro é válido:  
  - Um tabuleiro válido é uma lista contendo três linhas, cada uma com três valores, sendo `X`, `O` ou `EMPTY`.

### Restrições  
- A função `result(board)` não deve modificar o tabuleiro de entrada `board`.  
  - O algoritmo Minimax exige que se analisem vários estados diferentes do tabuleiro, então modificar diretamente o tabuleiro original está incorreto.  

- A forma como as funções foram declaradas não devem ser alteradas (nem a ordem e nem a quantidade dos argumentos).

## Executando o Jogo  
Depois que todas as funções forem implementadas corretamente, o jogo pode ser executado com:

```bash
python runner.py
```
Você poderá jogar contra a IA. E, como o *Jogo da Velha* sempre termina em empate quando ambos os jogadores jogam de forma ideal, você nunca conseguirá vencê-la (mas, se não jogar de forma ideal, ela poderá vencer você!).

## Dicas
- Para testar funções individuais, você pode importá-las em outro arquivo Python:

```python
from tictactoe import initial_state, player, ...
```
- Você pode adicionar funções auxiliares à `tictactoe.py`, desde que seus nomes não entrem em conflito com funções ou variáveis já existentes no módulo.

- A algoritmo **Alpha-beta pruning** é opcional, mas pode tornar a IA mais eficiente.

## Fonte
Este README foi baseado na documentação do projeto *Tic-Tac-Toe* do curso de Inteligência Artificial da Harvard, disponível em: [https://cs50.harvard.edu/ai/2024/projects/0/tictactoe/](https://cs50.harvard.edu/ai/2024/projects/0/tictactoe/).