Este README também está disponível em [inglês](README.md).
# Normais
## Contexto

Conforme citado em [Normals](https://cs50.harvard.edu/sql/2024/psets/0/normals/) – CS50: Introdução a Bancos de Dados com SQL:

> “Após o novo recorde anual de calor registrado em 2022 — o mais recente de uma série de anos com recordes — as temperaturas médias da superfície oceânica ao redor do mundo dispararam desde o início de março. Excluindo as regiões polares, elas estão cerca de dois décimos de grau Celsius mais quentes do que os cientistas já observaram nessa época do ano com base em dados de satélite.”  
>  
> — [The Washington Post](https://www.washingtonpost.com/climate-environment/2023/04/28/ocean-temperatures-heat-record-surge-climate/) (adaptado), 28 de abril de 2023 

Para determinar se as temperaturas oceânicas estão fora do padrão, cientistas utilizam uma métrica conhecida como *Climatologia Normal* (*Climate Normal*), que representa padrões climáticos de longo prazo com base em períodos de 30 anos. Um dos principais indicadores dessa métrica é a temperatura oceânica.

## Descrição do Problema

Este projeto envolve a análise de dados contidos no banco de dados `normals.db`, especificamente na tabela `normals`, para examinar dados recentes de Climatologia Normal e entender melhor as características das temperaturas oceânicas normais ao redor do mundo. A tarefa consiste em escrever consultas SQL que respondam a uma série de perguntas sobre esses dados.

## Conjunto de Dados

Para este problema, é fornecido o banco de dados `normals.db`, juntamente com *dez* arquivos `.sql` vazios.

A única tabela `normals` dentro de `normals.db` contém as seguintes colunas:

- `id`: identifica unicamente cada linha da tabela.
- `latitude`: o grau de latitude — expresso em formato decimal.
- `longitude`: o grau de longitude — expresso em formato decimal.
- `0m`: a temperatura normal da superfície oceânica (ou seja, a temperatura normal a 0 metros de profundidade), em graus Celsius, na coordenada.
- `5m`: a temperatura normal a 5 metros de profundidade, em graus Celsius, na coordenada.
- `10m`: a temperatura normal a 10 metros de profundidade, em graus Celsius, na coordenada.

As observações continuam até `5500m` para algumas coordenadas.

## Especificação

- Cada consulta deve consistir em uma única instrução `SELECT`.
- Nenhuma suposição deve ser feita sobre os valores da coluna `id` — as consultas devem continuar válidas independentemente desses valores.
- Cada consulta deve retornar **apenas** os dados necessários para responder à pergunta.
- Cada consulta SQL deve ser escrita em um arquivo separado, nomeado conforme o número da pergunta (ex: `1.sql` para a pergunta 1, `2.sql` para a pergunta 2, e assim por diante).

## Perguntas

Abaixo está a lista das 10 perguntas respondidas com consultas SQL:  

- [X] **Q1:** Encontre a temperatura normal da superfície oceânica no [Golfo do Maine](#golfo), na costa de Massachusetts.
- [X] **Q2:** Encontre a temperatura normal do [sensor mais profundo](#sensor) próximo ao Golfo do Maine, na mesma coordenada acima.
- [X] **Q3:** Escolha uma localização de sua preferência e encontre a temperatura normal a 0 metros, 100 metros e 200 metros.
- [X] **Q4:** Encontre a menor temperatura normal da superfície oceânica.
- [X] **Q5:** Encontre a maior temperatura normal da superfície oceânica.
- [X] **Q6:** Retorne todas as temperaturas normais do oceano a 50m de profundidade, bem como seus respectivos graus de latitude e longitude, dentro do Mar Arábico. Inclua as colunas latitude, longitude e temperatura. Considere que o Mar Arábico está delimitado pelas seguintes quatro coordenadas:
    - 20° de latitude, 55° de longitude
    - 20° de latitude, 75° de longitude
    - 0° de latitude, 55° de longitude
    - 0° de latitude, 75° de longitude
- [X] **Q7:** Encontre a temperatura média da superfície oceânica ao longo do equador, arredondada para duas casas decimais. Nomeie a coluna resultante como “Temperatura Média da Superfície no Equador”.
- [X] **Q8:** Encontre as 10 localizações com as menores temperaturas normais da superfície oceânica, ordenadas da mais fria para a mais quente. Caso duas localizações tenham a mesma temperatura, ordene por latitude, do menor para o maior valor. Inclua latitude, longitude e temperatura da superfície.
- [X] **Q9:** Encontre as 10 localizações com as maiores temperaturas normais da superfície oceânica, ordenadas da mais quente para a mais fria. Caso duas localizações tenham a mesma temperatura, ordene por latitude, do menor para o maior valor. Inclua latitude, longitude e temperatura da superfície.
- [X] **Q10:** Existem 180 graus inteiros de latitude. Para esta pergunta, determine quantos pontos de latitude possuem ao menos um dado registrado. (Por que será que não há dados para todas as latitudes?)

## Dicas fornecidas

```
Como a tabela normals é ampla, considere usar SELECT apenas para latitude, longitude e algumas colunas de profundidade.
```


- A temperatura normal da superfície está na coluna `0m`, que corresponde a 0 metros de profundidade!
<a name="golfo"></a>
- O **Golfo do Maine** está na latitude 42.5° e longitude -69.5°.
<a name="sensor"></a>
- O **sensor mais profundo** próximo ao Golfo do Maine registra dados a 225 metros de profundidade, ou seja, os dados estão na coluna `225m`.
- As temperaturas da superfície oceânica no equador podem ser encontradas em todas as longitudes entre as latitudes -0.5° e 0.5°, inclusive.
- O Google Earth pode ser útil para encontrar coordenadas.

## Fonte

Este README foi baseado na documentação do problema *Normals* do curso **CS50: Introdução a Bancos de Dados com SQL**, da Universidade Harvard, disponível em: [https://cs50.harvard.edu/sql/2024/psets/0/normals/](https://cs50.harvard.edu/sql/2024/psets/0/normals/)


