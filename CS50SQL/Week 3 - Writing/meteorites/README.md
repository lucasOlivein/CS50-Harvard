# Meteorite Cleaning

### 🚀 Summary
...
### 📄 Description (Adapted)
...
### ⚙️ Specification

📌 **Task**: In `import.sql`, write a series of SQL (and SQLite) statements to import and clean the data from `meteorites.csv` into a table, `meteorites`, in a database called `meteorites.db`.


<details><summary>📋 <strong>Requirements</strong></summary>

---

- <details><summary> ✅ Within <code>meteorites.db</code>, the meteorites table should have the following columns:</summary>

    --- 
    - `id`, which represents the unique ID of the meteorite.
    - `name`, which represents the given name of the meteorite.
    - `class`, which is the classification of the meteorite, according to the traditional classification scheme.
    - `mass`, which is the weight of the meteorite, in grams.
    - `discovery`, which is either “Fell” or “Found”. “Fell” indicates the meteorite was seen falling to Earth, whereas “Found” indicates the meteorite was found only after landing on Earth.
    - `year`, which is the year in which the the meteorite was discovered.
    - `lat`, which is the latitude at which the meteorite landed.
    - `long`, which is the longitude at which the meteorite landed.

    ---
    </details>



-  ✅  Any empty values in `meteorites.csv` are represented by `NULL` in the `meteorites` table. 
    - Keep in mind that the following columns have empty values in the CSV: `mass`, `year`, `lat`, and `long` 
-   ✅  All columns with decimal values (e.g., 70.4777) should be rounded to the nearest hundredths place (e.g., 70.4777 becomes 70.48). 
    - Keep in mind that the following columns have decimal values: `mass`, `lat`, and `long`.
-   ✅  All meteorites with the `nametype` “Relict” are not included in the `meteorites` table.
-   ✅  The meteorites are sorted by `year`, oldest to newest, and then—if any two meteorites landed in the same year—by `name`, in alphabetical order.
-   ✅  You’ve updated the IDs of the meteorites from `meteorites.csv`, according to the order specified in #4. 
    - The `id` of the meteorites should start at 1, beginning with the meteorite that landed in the oldest year and is the first in alphabetical order for that year.
</details>

<details><summary> ✦ <strong>Advice</strong></summary>

---
- <details><summary> Begin by importing <code>meteorites.csv</code> into a temporary table</summary>

    ---
    Start by getting all of the data from `meteorites.csv` into a temporary table, one called `meteorites_temp`. A temporary table is a helpful placeholder: _you can use it to clean your data until it’s in a form that’s suitable for your final meteorites table._

    Before you import a CSV into a SQLite database, it’s best to define the schema for the table into which that data will be imported. In import.sql, then, try the following:

    ```sql
    CREATE TABLE "meteorites_temp" (
    -- TODO
    );
    ```
    We’ll leave the column names up to you.

    Next, recall that `.import` is a SQLite statement that can import a CSV into a table of your choice. After your `CREATE TABLE` statement, write a `.import` statement to import the data from `meteorites.csv` into the `meteorites_temp` table.

    Finally, try creating `meteorites.db` by running the statements in `import.sql`.

    ---

    </details>

- <details><summary>Write SQL statements to clean the imported data</summary>

    ---
    With your data in a temporary table, continue writing SQL statements to clean the data. Consider how you might update the values of the `mass` column for instance:
    ```sql
    UPDATE "meteorites_temp"
    SET "mass" = ...
    WHERE ...
    ```
    You might need to write a few such statements, one (or more) for each column you’re trying to clean.

    --- 

    </details>

- <details><summary>Transfer the data from your temporary table into a meteorites table</summary>

    ---
    Recall that you can `INSERT` values into a new table by `SELECT`ing rows from another:
    ```sql
    INSERT INTO "table0" ("column0", "column1")
    SELECT "column0", "column1" FROM "table1";
    ```

    _When you do so, you can re-order your data using ORDER BY. And, so long as you’ve specified a primary key column in your new table, such a statement will auto-assign new IDs to the inserted rows if none is specified._ 

    Once you’re done with the temporary table, it’s good practice to drop it!
    </details>

---
</details>

### 🎯 Solution
| Step | Commit |
|----------|--------|
| Drop temporary staging table | [68cf361](https://github.com/lucasOlivein/CS50-Harvard/commit/68cf3610943192f8a5ef6e8683d5e5031502cf11)  |
| Load cleaned records into final table | [45aed7c](https://github.com/lucasOlivein/CS50-Harvard/commit/45aed7c0ac540500bc8d3b892ee6b826e807d95d) |
| Create final `meteorites` table | [342de3c](https://github.com/lucasOlivein/CS50-Harvard/commit/342de3cc85cf51987b5a1e76f78452b392d614ba) |
| Exclude entries where `nametype = 'Relict'` | [af255bd](https://github.com/lucasOlivein/CS50-Harvard/commit/af255bd0918ca3872e7ca471ca4d308986451b9e) |
| Round numeric fields to 2 decimal places | [6f106fc](https://github.com/lucasOlivein/CS50-Harvard/commit/6f106fc8b8cf9344a68c95724d2c637e9c5f21bd) |
| Convert empty strings to NULL | [6a2c2d5](https://github.com/lucasOlivein/CS50-Harvard/commit/6a2c2d50c2ff19b5aa1f97e765ff1d1f8388d545) |
| Import CSV data into staging table | [efd4547](https://github.com/lucasOlivein/CS50-Harvard/commit/efd45470a91950c6e4208a08f77e5d1566a1780c) |
| Create temporary staging table | [559ef80](https://github.com/lucasOlivein/CS50-Harvard/commit/559ef800f1e3c77bbc9695543067c7e898e30ff0) |

### 📚 Source
_Meteorite Cleaning_ from Harvard’s CS50 SQL course: https://cs50.harvard.edu/sql/psets/3/meteorites/

### 📂 Download
Distribution code: https://cdn.cs50.net/sql/2024/x/psets/3/meteorites.zip