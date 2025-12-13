# 🗓 Week 1 - Relating

_Problem Set 1:_
📌 Submit the problems bellow.

## 📝 Problems

- ⬜ Packages, Please
- ⬜ DESE
- ⬜ Moneyball

🔗 [View assignment page →](https://cs50.harvard.edu/sql/psets/1/#problem-set-1)

## 🏷️ Topics


<details><summary><strong>Relatioships</strong></summary>
    
- One-to-one 
- One-to-many
- Many-to-many

</details>


<details><summary><strong>Entity Relationship Diagrams</strong></summary>

- Crow's foot notation

</details>


<details><summary><strong>Keys</strong></summary>

- Primary Key
- Forein Key 

</details>

<details><summary><strong>Subqueries</strong></summary>

_Also called nested queries._   
_The querie fursthest inside the parentheses will run first._

- <details><summary>Nested queries</summary>

    - <details><summary>One-to-many</summary>

        ```sql        
        SELECT "title"
        FROM "books"
        WHERE "publisher_id" = (
            SELECT "id"
            FROM "publishers"
            WHERE "publisher" = 'Fitzcarraldo Editions'
        );
        ``` 
        </details>


    - <details><summary>Many-to-many</summary>

        ```sql
        SELECT "name"
        FROM "authors"
        WHERE "id" = (
            SELECT "author_id"
            FROM "authored"
            WHERE "book_id" = (
                SELECT "id"
                FROM "books"
                WHERE "title" = 'Flights'
            )
        );
        ```
        </details>

    </details>

- <details><summary><strong>IN</strong> clasule</summary>

    _Used in the `WHERE` clasule to say: SELECT ... FROM ... WHERE `<expression> IN <set_or_subquery>`_
    ```sql
    SELECT "title"
    FROM "books"
    WHERE "id" IN (
        SELECT "book_id"
        FROM "authored"
        WHERE "author_id" = (
            SELECT "id"
            FROM "authors"
            WHERE "name" = 'Fernanda Melchor'
        )
    );
    ```
    </details>

</details>


<details><summary><strong>Joins</strong></summary>

- <details><summary>Inner Join</summary>

    ```sql
    SELECT *
    FROM "sea_lions"
    JOIN "migrations" ON "migrations"."id" = "sea_lions"."id";
    ```
    _or_
    ```sql
    SELECT *
    FROM "sea_lions"
    INNER JOIN "migrations" ON "migrations"."id" = "sea_lions"."id";
    ```
    </details>

- <details><summary>Outer joins</summary>

    - LEFT JOIN
    - RIGHT JOIN
    - FULL JOIN
    </details>

- <details><summary>Natural Join</summary>

    _It's used when two tables share one or more columns with the same name_. 
    _In this example, the `NATURAL JOIN` is performed using the shared `id` column_:
    ```sql
    SELECT *
    FROM "sea_lions"
    NATURAL JOIN "migrations";
    ```
    </details>
</details>

<details><summary><strong>Sets</strong></summary>

- <details><summary>INTERSECT</summary>

    ```sql
    SELECT "book_id" FROM "translated"
    WHERE "translator_id" = (
        SELECT "id" from "translators"
        WHERE "name" = 'Sophie Hughes'
    )
    INTERSECT
    SELECT "book_id" FROM "translated"
    WHERE "translator_id" = (
        SELECT "id" from "translators"
        WHERE "name" = 'Margaret Jull Costa'
    );
    ```
    </details>

- <details><summary>UNION</summary>

    ```sql
    SELECT 'author' AS "profession", "name" 
    FROM "authors"
    UNION
    SELECT 'translator' AS "profession", "name" 
    FROM "translators";
    ```
    </details>

- <details><summary>EXCEPT</summary>

    ```sql
    SELECT "name" FROM "authors"
    EXCEPT
    SELECT "name" FROM "translators";
    ```
    </details>

</details>


<details><summary><strong>Groups</strong></summary>

- <details><summary>GROUP BY</summary>

    ```sql
    SELECT "book_id", AVG("rating") AS "average rating"
    FROM "ratings"
    GROUP BY "book_id";
    ```
    </details>

- <details><summary>HAVING</summary>

    ```sql
        SELECT "book_id", ROUND(AVG("rating"), 2) AS "average rating"
        FROM "ratings"
        GROUP BY "book_id"
        HAVING "average rating" > 4.0;
    ```
    </details>

</details>
