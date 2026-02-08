# 🗓 Week 3 - Viewing

📌**Problem Set 4**: _Submit the problems bellow._

## 📝 Problems

- ⬜ [Census Taker](./census/)
- ⬜ [The Private Eye](./private/)
- ⬜ [Bed and Breakfast](./bnb/)

## 🏷️ Topics



- <details><summary><strong>Views</strong></summary>

    ---

    A view is a virtual table defined by a query.     
    As an example of a query to join three tables and select the relevant columns: 
    ```sql
    SELECT "name", "title" FROM "authors"
    JOIN "authored" ON "authors"."id" = "authored"."author_id"
    JOIN "books" ON "books"."id" = "authored"."book_id";
    ```
    
    The new table created by this query can be saved as a view:
    ```sql
    CREATE VIEW "longlist" AS
    SELECT "name", "title" FROM "authors"
    JOIN "authored" ON "authors"."id" = "authored"."author_id"
    JOIN "books" ON "books"."id" = "authored"."book_id";
    ```
    
    And then, be further queried later on as a table:
    ```sql
    SELECT * FROM "longlist";
    ```    

    Each time a view is created, it gets added to the schema, that is, it can be verifying by running `.schema`.

    As a virtual table, a view does not consume much more disk space to create. The data within a view is still stored in the underlying tables, but still accessible through this simplfied view.

    Views are useful for:

    - <details><summary><strong>Simpliflying</strong></summary>

        ---

        Putting together data from different tables to be queried more simply.

        As an example of a complex query:
        ```sql
        SELECT "title" FROM "books"
        WHERE "id" IN (
            SELECT "book_id" FROM "authored"
            WHERE "author_id" = (
                SELECT "id" FROM "authors"
                WHERE "name" = 'Fernanda Melchor'
            )
        );
        ```
        This can be simplified by using a view:
        ```sql
        CREATE VIEW "longlist" AS
        SELECT "name", "title" FROM "authors"
        JOIN "authored" ON "authors"."id" = "authored"."author_id"
        JOIN "books" ON "books"."id" = "authored"."book_id";
        ```
        And then queried as:
        ```sql
        SELECT "title" FROM "longlist" WHERE "name" = 'Fernanda Melchor';
        ```

        ---
        </details>
    
    - <details><summary><strong>Aggregating</strong></summary>

        ---
        Running aggregate functions, like finding the sum, and storing the results.

        As an example, the following query:
        ```sql        
        SELECT "book_id", "title", "year", ROUND(AVG("rating"), 2) AS "rating" 
        FROM "ratings"
        JOIN "books" ON "ratings"."book_id" = "books"."id"
        GROUP BY "book_id";
        ```
        Can be stored as a view:
        ```sql
        CREATE VIEW "average_book_ratings" AS
        SELECT "book_id" AS "id", "title", "year", ROUND(AVG("rating"), 2) AS "rating" 
        FROM "ratings"
        JOIN "books" ON "ratings"."book_id" = "books"."id"
        GROUP BY "book_id";
        ```

        And, on adding more data to the ratings table, to obtain an up-to-date aggregate, we need to simply requery the view using a SELECT command!

        ---
        </details>
    - <details><summary><strong>Partitioning</strong></summary>
        
        ---
        Dividing data into logical pieces.

        Views can be used to partition data, or to break it into smaller pieces that will be useful to us or an application. 
        
        As an example of longlisted books stored in a single table, the data can be partitioned by year using views such as:
        ```sql
        CREATE VIEW "2022" AS
        SELECT "id", "title" FROM "books"
        WHERE "year" = 2022;
        ``` 
        In this case, the virtual table contains only books from the year 2022.

        ---

        </details>

    - <details><summary><strong>Securing</strong></summary>
        
        ---
        Hiding columns that should be kept secure. 

        We can create a view with the relevant columns while omitting sensitive ones entirely.

        As an example:
        ```sql
        CREATE VIEW "analysis" AS
        SELECT "id", "origin", "destination", 'Anonymous' AS "rider" 
        FROM "rides";
        ```
        In this example, the rider column is replaced with an anonymous value for each row. This indicates that, although rider names exist in the database, they have been anonymized for security purposes.

        Although we can create a view that anonymizes data, SQLite does not allow access control. This means that, in this case, a simple query on the original `rides` table could still retrieve all the rider names.

        ---
        </details>

    <details><summary><strong>Soft Deletions</strong></summary>
        
    ---

    A soft deletion involves marking a row as deleted instead of removing it from the table.

    As an example, in the `collections` table, we add a `deleted` column:
    ```sql
    ALTER TABLE "collections" 
    ADD COLUMN "deleted" INTEGER DEFAULT 0;
    ```
    We then create a view to display only the rows that have not been deleted:
    ```sql
    CREATE VIEW "current_collections" AS
    SELECT "id", "title", "accession_number", "acquired" 
    FROM "collections" 
    WHERE "deleted" = 0;
    ```

    Finally, the data can be retrieved with:

    ```sql
    SELECT * FROM "current_collections";
    ```

    ---
    </details>

    <details><summary><strong>Insertion and Deletion</strong></summary>

    ---
    It is not possible to insert data into or delete data from a view.   
    However, we can set up a trigger that inserts into or deletes from the underlying table!

    The `INSTEAD OF` trigger allows us to do this.

    - <details><summary><strong>Delete</strong></summary>

        ---
        ```sql
        CREATE TRIGGER "delete"
        INSTEAD OF DELETE ON "current_collections"
        FOR EACH ROW
        BEGIN
            UPDATE "collections" SET "deleted" = 1 
            WHERE "id" = OLD."id";
        END;
        ```
        - Every time we try to delete rows from the view, this trigger will instead update the deleted column of the row in the underlying table collections, thus completing the soft deletion.
        - We use the keyword `OLD` within our update clause to indicate that the ID of the row updated in `collections` should be the same as the ID of the row we are trying to delete from `current_collections`.
        ---

        </details>
    
    - <details><summary><strong>Insert</strong></summary>

        ---
        We can create a trigger that inserts data into the underlying table when we try to insert it into a view.

        There are two situations to consider:

        - <details><summary><strong>Insert a row that was soft deleted:</strong></summary>

            ---
            ```sql
            CREATE TRIGGER "insert_when_exists"
            INSTEAD OF INSERT ON "current_collections"
            FOR EACH ROW 
            WHEN NEW."accession_number" IN (
                SELECT "accession_number" FROM "collections"
            )
            BEGIN
                UPDATE "collections" 
                SET "deleted" = 0 
                WHERE "accession_number" = NEW."accession_number";
            END;
            ```

            - The `WHEN` keyword is used to check if the accession number of the artwork already exists in the collections table. This works because an accession number, as we know from previous weeks, uniquely identifies every piece of art in this table.
            - If the artwork does exist in the underlying table, we set its deleted value to 0, indicating a reversal of the soft deletion.

            ---

            </details>

        - <details><summary><strong>Insert a row that does not exist in the underlying table:</strong></summary>

            ---
            ```sql
            CREATE TRIGGER "insert_when_new"
            INSTEAD OF INSERT ON "current_collections"
            FOR EACH ROW
            WHEN NEW."accession_number" NOT IN (
                SELECT "accession_number" FROM "collections"
            )
            BEGIN
                INSERT INTO "collections" ("title", "accession_number", "acquired")
                VALUES (NEW."title", NEW."accession_number", NEW."acquired");
            END;
            ```
            - When the accession number of the inserted data is not already present within collections, it inserts the row into the table.
            ---
            </details>


        </details>
    

    ---

    </details>


    ---
    </details>


- <details><summary><strong>Temporary view</strong></summary>

    ---

    A temporary view is a view that exists only for the duration of our connection with the database.

    To create temporary views that are not stored in the database schema, we can use `CREATE TEMPORARY VIEW`:
    ```sql
    CREATE TEMPORARY VIEW "average_ratings_by_year" AS
    SELECT "year", ROUND(AVG("rating"), 2) AS "rating" FROM "average_book_ratings" 
    GROUP BY "year";
    ```

    ---
    </details>


- <details><summary><strong>Common Table Expression (CTE)</strong></summary>

    ---
    A regular view exist forever in our database schema.   
    A temporary view exists for the duration of our connection with the database.      
    A `CTE` is view that exist for a single query alone:

    ```sql
    WITH "average_book_ratings" AS (
        SELECT "book_id", "title", "year", ROUND(AVG("rating"), 2) AS "rating" FROM "ratings"
        JOIN "books" ON "ratings"."book_id" = "books"."id"
        GROUP BY "book_id"
    )
    SELECT "year", ROUND(AVG("rating"), 2) AS "rating" FROM "average_book_ratings"
    GROUP BY "year";
    ```

    ---
    </details>

    