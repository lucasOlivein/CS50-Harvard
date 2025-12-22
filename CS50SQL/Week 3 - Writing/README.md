# 🗓 Week 3 - Writting

📌**Problem Set 3**: _Submit the problems bellow._


## 📝 Problems

-  ✅ [Don’t Panic!](./dont-panic/)
-  ✅ [Meteorite Cleaning](./meteorites/)

## 🏷️ Topics

- <details><summary><strong>Importing Data</strong></summary>

    ---
    _SQLite makes it possible to import a CSV file directly into our database. To do this, we need to start from scratch._

    ```sqlite
    .import --csv --skip 1 mfa.csv collections
    ```
    - _The first argument, --csv indicates to SQLite that we are importing a CSV file. This will help SQLite parse the file correctly._
    - _The second argument indicates that the first row of the CSV file (the header row) needs to be skipped, or not inserted into the table._


    <details><summary><strong>Importing into an existing table</strong></summary>

    ---
    - The CSV file must have the same number of columns as the table and in the same order.
    - Otherwise, to successfully import the CSV file, we will need to use a temporary table.
    ```bash
    .import --csv mfa.csv temp
    ```
    - Next, we will select the data from temp and insert it into the target table.
    </details>

    --- 

    </details>

- <details><summary><strong>Foreign Key Deletion Actions</strong></summary>

    --- 

    ```sql
    FOREIGN KEY("collection_id") REFERENCES "collections"("id") ON DELETE <action>

    -- Example
    FOREIGN KEY("artist_id") REFERENCES "artists"("id") ON DELETE CASCADE
    ```

    <details><summary><code>RESTRICT</code></summary>

    - _This restricts us from deleting IDs when the foreign key constraint is violated._
    </details>

    <details><summary><code>NO ACTION</code></summary>

    - _This allows the deletion of IDs that are referenced by a foreign key and nothing happens._
    </details>

    <details><summary><code>SET NULL</code></summary>

    - _This allows the deletion of IDs that are referenced by a foreign key and sets the foreign key references to `NULL`._
    </details>

    <details><summary><code>SET DEFAULT</code></summary>

    - _This does the same as the previous, but allows us to set a default value instead of `NULL`._
    </details>

    <details><summary><code>CASCADE</code></summary>

    - _This allows the deletion of IDs that are referenced by a foreign key and also proceeds to cascadingly delete the referencing foreign key rows. For example, if we used this to delete an artist ID, all the artist’s affiliations with the artwork would also be deleted from the `created` table._
    </details>

    --- 
    </details>


- <details><summary><strong>Triggers</strong></summary>

    ---
    - _A trigger is a SQL statement that runs automatically in response to another SQL statement, such as an `INSERT`, `UPDATE`, or `DELETE`._

    - _Triggers are useful for maintaining data consistency and automating tasks across related tables._

    <details><summary><strong>Example</strong></summary>
    
    ---
    ```sql
    CREATE TRIGGER "sell" 
    BEFORE DELETE ON "collections"
    BEGIN
    INSERT INTO "transactions" ("title", "action")
    VALUES (OLD."title", 'sold');
    END;
    ```

    - This trigger runs before a row is deleted from `collections`.
    - **OLD** is a special keyword that refers to the row being deleted.
    - `OLD."title"` accesses the title column of the row about to be deleted.
    - The trigger automatically inserts a record into `transactions` with the action “sold”.
    </details>

    ---
    
    </details>


- <details><summary><strong>Soft Deleting</strong></summary>
    
    ---
    _**Soft deletion** (or a **soft delete**) means marking data as deleted rather than actually removing it from the database._

    <details><summary><strong>Example</strong></summary>
    
    ---
    _We could add a deleted column to the collections table with a default value of 0:_
    ```sql
    ALTER TABLE "collections"
    ADD COLUMN "deleted" INTEGER DEFAULT 0;
    ```
    _To “delete” a row, we would update the deleted column to 1:_
    ```sql
    UPDATE "collections"
    SET "deleted" = 1
    WHERE "title" = 'Farmers working at dawn';
    ```
    _Then, to query only non-deleted rows:_
    ```sql
    SELECT * FROM "collections"
    WHERE "deleted" != 1;
    ```
    _This way, data can be recovered if needed and maintains a complete historical record._

    _However, it’s still important to comply with data privacy regulations that require data to be truly deleted._

    ---

    </details>
    </details>



## `</>` Syntax

<details><summary><code>INSERT</code></summary>

---
```sql
INSERT INTO "collections" ("id", "title", "accession_number", "acquired")
VALUES (1, 'Profusion of flowers', '56.257', '1956-04-12');
```
_This command requires the list of columns in the table that will receive new data and the values to be added to each column, in the same order._


- <details><summary><strong>Inserting Multiple Rows</strong></summary>

    ```sql
    INSERT INTO table (column0, ...)
    VALUES
    (value0, ...),
    (value1, ...),
    ...;
    ```
    _Inserting multiple rows at once in this manner allows the programmer some convenience. It is also a faster, more efficient way of inserting rows into a database._
    </detauls>


---

</details>

<details><summary><code>DELETE</code></summary>

---

```sql
-- Delete a specific row
DELETE FROM "collections"
WHERE "title" = 'Spring outing';

-- Delete any row with NULL in the acquired column
DELETE FROM "collections"
WHERE "acquired" IS NULL;

-- Delete all rows
DELETE FROM "collections";
```



---
</details>

<details><summary><code>UPDATE</code></summary>

---
```sql
UPDATE <table>
SET <column0> = <value0>, ...
WHERE <condition>;

-- Example


UPDATE "created"
SET "artist_id" = (
    SELECT "id"
    FROM "artists"
    WHERE "name" = 'Li Yin'
)
WHERE "collection_id" = (
    SELECT "id"
    FROM "collections"
    WHERE "title" = 'Farmers working at dawn'
);
```

- _The first part of this query specifies the table to be updated._
- _The next part retrieves the ID of Li Yin to set as the new ID._
- The last part selects the row(s) in created which will be updated with the ID of Li Yin, which is the painting “Farmers working at dawn”!

---

</details>

