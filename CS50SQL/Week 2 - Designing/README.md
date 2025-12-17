# 🗓 Week 2 - Designing

_Problem Set 2:_
📌 Submit the problems bellow.

## 📝 Problems

- ⬜ ATL
- ⬜ Happy to Connect
- ⬜ Union Square Donuts

🔗 [View assignment page →](https://cs50.harvard.edu/sql/psets/2/#problem-set-2)

## 🏷️ Topics




<details><summary><strong>Normalizing</strong></summary>

<br>

_The process of separating the data, puting each entity in its own table.   
Any information about a specific entity goes into the entity’s own table._
- Reduce redundancies

---
</details>

<details><summary><strong>Storage Class and Data Types</strong></summary>

<br>

_SQLite defines five storage classes, each designed to hold specific data types:_

<!-- NULL -->
- <details><summary><strong>Null: </strong><em>nothing, or empty value</em></summary>

    <br>

    - Any column can contain `NULL`

    - <details><summary><code>IS NULL</code> and <code>IS NOT NULL</code> are used for comparison.</summary>

        ```sql
        SELECT * FROM usuarios WHERE email IS NULL;
        ```
        ```sql
        SELECT * FROM usuarios WHERE email IS NOT NULL;
        ```

        </details>

        - <details><summary><em> Common comparisons don't work</em></summary>
            
            ```sql
            SELECT * FROM usuarios WHERE email = NULL; -- Doesn't work
            ```

            </details>

    - <details><summary>Arithmetic operations involving <code>NULL</code> results in <code>NULL</code></summary>

        ```sql
        SELECT 10 + NULL;  -- result: NULL
        ```
    
        </details>

    </details>

<!-- END NULL -->

<!-- Integer -->
- <details><summary><strong>Integer:</strong> <em>numbers without decimal points</em></summary>

    <br>

    - `INTEGER` values are stored using **1**, **2**, **3**, ****4**, **6**, or **8** bytes

    - <details><summary>Operations with <code>INTEGER</code></summary>

        ```sql
        SELECT 10 / 3;     -- 3  (INTEGER if both are INTEGER)
        SELECT 10.0 / 3;   -- 3.333... (REAL)
        ```
        </details>

    - <details><summary> <code>INTEGER</code> type affinities</summary>

        <br>

        - `INTEGER`
        - `INT`
        - `SMALLINT`
        - `BIGINT`
        - `TINYINT`

        </details>
    </details>
<!-- END Integer -->

<!-- Real -->
- <details><summary><strong>Real:</strong> <em>decimal or floating point numbers</em></summary>

    <br>

    - **15** to **17** decimal digits of precision.
    
    - <details><summary>Comparisons with <code>REAL</code> values may be affected by precision.</summary>

        ```sql
        SELECT * FROM produtos WHERE preco = 0.3; -- may fail
        ```
        </details>
    - <details><summary> Aritmetic operations with <code>REAL</code> result in <code>REAL</code>.</summary>


        ```sql
        SELECT 10 / 3;      -- 3 (INTEGER)
        SELECT 10 / 3.0;    -- 3.3333333333333335
        SELECT 10.0 / 3;    -- 3.3333333333333335
        ```
        </details>
    
    - <details><summary><code>REAL</code> type affinities</summary>

        <br>

        - `REAL`
        - `DOUBLE`
        - `DOUBLE PRECISION`
        - `FLOAT`
        </details>
<!-- END Real -->

<!-- TEXT -->
- <details><summary><strong>Text:</strong> <em>characters or strings</em></summary>

    <br>

    - <details><summary>The practical limit is the maximum string size</summary>

        <br>

       -  _By default can reach approximately 1 GB (configurable at compile time)._

    - <details><summary>Unicode Encodings</summary>

        <br>

        - UTF-8 _(default)_
        - UTF-16LE
        - UTF-16BE
        </details>

    - `TEXT` comparisons are performed **lexicographically**.
    - <details><summary>Ordering depend on the <strong>collation</strong> (sorting).</summary>

        <br>

        - Collarion types:
            - `BINARY` (padrão)
            - `NOCASE`
            - `RTRIM`

        <details><summary><strong>Example:</strong></summary>

        ```sql
        SELECT * FROM usuarios ORDER BY nome COLLATE NOCASE;
        ```

        </details>

        </details>
    - <details><summary><code>TEXT</code> type affinities</summary>
        
        <br>
        
        - `TEXT`
        - `CHAR`
        - `CHARACTER`
        - `VARCHAR`
        - `CLOB`
        
        </details>


    </details>
<!-- END TEXT -->

- <details><summary><strong>Blob:</strong> <em> store objects in binary</em></summary>

    <br>

    - Store sequences of bytes with no type interpretation or encoding by SQLite
        - <details><summary><strong>Usage examples:</strong></summary>

            <br>

            - Images (PNG, JPG)
            - PDF files
            - Audio or video
            - Encrypted data
            - Compressed content

            </details>
    - The default size limit is close to 1 GB per value (depending on the configuration).
    - `BLOB` does not impose any **type affinity**.
    - <details><summary>Comparisons are performed <strong>byte by byte</strong>.</summary>

        <br>

       -  _There is no semantic ordering, only binary ordering._

        </details>

    </details>

----
</details>

<details><summary><strong>Type Affinities</strong></summary>

<br>

_SQLite don’t always store one particular data type. They are said to have **type affinities**, meaning that they try to convert an input value into the type they have an affinity for._

- Column types is defined at table creation time.
- The five type affinities in SQLite correspond to the five storage classes.
<details><summary><strong>Examples:</strong></summary>

- <details><summary><em>A column with a type affinity for Integers</em></summary> 

    - If we try to insert `'25'` (the number 25 but stored as text) into this column, it will be converted into an integer data type.

    </details>

- <details><summary><em>A column with a type affinity for Text</em></summary>

    - If we tray insert an integer `25` into this column, it will be converted into the text equivalent, `'25'`.

    </details>
</details>


---

</details>

<details><summary><strong>Table Constraints</strong></summary>

<br>

_Used to enforce rules and restrictions on data stored in tables.
There are four types of table constraints:_

- `PRIMARY KEY`
- `FOREIGN KEY`
- `UNIQUE`
- `CHECK`

<details><summary><strong>Example:</strong></summary>

```sql
CREATE TABLE orders (
    id INTEGER,
    user_id INTEGER,
    amount REAL,
    status TEXT,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    UNIQUE (user_id, id),
    CHECK (amount > 0)
);

```

</details>

---

</details>

<details><summary><strong>Column Constraints</strong></summary>

<br>

_Is a type of constraint that applies to a specified column in the table.     
In SQLite there are six types:_

- `CHECK`
- `DEFAULT`
- `NOT NULL`
- `UNIQUE`
- `PRIMARY KEY`
- `REFERENCES` <em>(foreign key)</em>

<details><summary><strong>Example:</strong></summary>

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    age INTEGER CHECK (age >= 18),
    country TEXT DEFAULT 'Brazil',
    role_id INTEGER REFERENCES roles(id)
);
```

</details>

---- 

</details>

<br>

### </> Syntax
<details><summary><strong>CREATE TABLE</strong></summary>

```sql
CREATE TABLE "swipes" (
    "id" INTEGER,
    "card_id" INTEGER,
    "station_id" INTEGER,
    "type" TEXT NOT NULL CHECK("type" IN ('enter', 'exit', 'deposit')),
    "datetime" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "amount" NUMERIC NOT NULL CHECK("amount" != 0),
    PRIMARY KEY("id"),
    FOREIGN KEY("station_id") REFERENCES "stations"("id"),
    FOREIGN KEY("card_id") REFERENCES "cards"("id")
);
```

</details>

<details><summary><strong>ALTER TABLE</strong></summary>



- <details><summary><code>RENAME TO</code></summary>

    ```sql
    ALTER TABLE "visits"
    RENAME TO "swipes";
    ```
    </details>
- <details><summary><code>RENAME COLUMN</code></summary>

    ```sql
    ALTER TABLE "swipes"
    RENAME COLUMN "swipetype" TO "type";
    ```
    </details>

- <details><summary><code>ADD COLUMN</code></summary>

    ```sql
    ALTER TABLE "swipes"
    ADD COLUMN "swipetype" TEXT;
    ```

    </details>
- <details><summary><code>DROP COLUMN</code></summary>

    ```sql
    ALTER TABLE "swipes"
    DROP COLUMN "type";
    ```

    </details>


</details>

<details><summary><strong>DROP TABLE</strong></summary>

```sql
DROP TABLE "riders";
```

</details>