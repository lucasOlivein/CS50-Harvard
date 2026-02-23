# your.harvard

### 🚀 Summary
...
### 📄 Description (Adapted)
...

### 🗃️ Schema
...


### ⚙️ Specification
📌 **Task**: In `indexes.sql`, write a set of SQL statements that create indexes which will speed up typical queries on the `harvard.db` database.    

- <details><summary>✔️ Typical <code>SELECT</code> queries on <code>harvard.db</code></summary>

    ---
    When engineers optimize a database, they often care about the typical queries run on the database. Such queries highlight patterns with which a database is accessed, thus revealing the best columns and tables on which to create indexes.

    - <details><summary>✅️ Find a student’s historical course enrollments, based on their ID:</summary>

        ---
        ```sql
        SELECT "courses"."title", "courses"."semester"
        FROM "enrollments"
        JOIN "courses" ON "enrollments"."course_id" = "courses"."id"
        JOIN "students" ON "enrollments"."student_id" = "students"."id"
        WHERE "students"."id" = 3;
        ```
        </details>

    - <details><summary>✅️Find all students who enrolled in Computer Science 50 in Fall 2023:</summary>

        ---
        ```sql
        SELECT "id", "name"
        FROM "students"
        WHERE "id" IN (
            SELECT "student_id"
            FROM "enrollments"
            WHERE "course_id" = (
                SELECT "id"
                FROM "courses"
                WHERE "courses"."department" = 'Computer Science'
                AND "courses"."number" = 50
                AND "courses"."semester" = 'Fall 2023'
            )
        );
        ```
        </details>

    - <details><summary>✅️ Sort courses by most- to least-enrolled in Fall 2023:</summary>

        ---
        ```sql
        SELECT "courses"."id", "courses"."department", "courses"."number", "courses"."title", COUNT(*) AS "enrollment"
        FROM "courses"
        JOIN "enrollments" ON "enrollments"."course_id" = "courses"."id"
        WHERE "courses"."semester" = 'Fall 2023'
        GROUP BY "courses"."id"
        ORDER BY "enrollment" DESC;
        ```
        </details>

    - <details><summary>✅️ Find all computer science courses taught in Spring 2024:</summary>

        ---
        ```sql
        SELECT "courses"."id", "courses"."department", "courses"."number", "courses"."title"
        FROM "courses"
        WHERE "courses"."department" = 'Computer Science'
        AND "courses"."semester" = 'Spring 2024';
        ```
        </details>

    - <details><summary>✅️ Find the requirement satisfied by “Advanced Databases” in Fall 2023:</summary>

        ---
        ```sql
        SELECT "requirements"."name"
        FROM "requirements"
        WHERE "requirements"."id" = (
            SELECT "requirement_id"
            FROM "satisfies"
            WHERE "course_id" = (
                SELECT "id"
                FROM "courses"
                WHERE "title" = 'Advanced Databases'
                AND "semester" = 'Fall 2023'
            )
        );
        ```
        </details>

    - <details><summary>✅️ Find how many courses in each requirement a student has satisfied:</summary>

        ---
        ```sql
        SELECT "requirements"."name", COUNT(*) AS "courses"
        FROM "requirements"
        JOIN "satisfies" ON "requirements"."id" = "satisfies"."requirement_id"
        WHERE "satisfies"."course_id" IN (
            SELECT "course_id"
            FROM "enrollments"
            WHERE "enrollments"."student_id" = 8
        )
        GROUP BY "requirements"."name";
        ```
        </details>

    - <details><summary>✅️ Search for a course by title and semester:</summary>

        ---
        ```sql
        SELECT "department", "number", "title"
        FROM "courses"
        WHERE "title" LIKE "History%"
        AND "semester" = 'Fall 2023';
        ```
        </details>

    </details>


⭐ **Note**: The number of indexes you create, as well as the columns they include, is entirely up to you. 





<details><summary>💎 <strong>Advice</strong></summary>

---
In this problem, you’ll take the opposite perspective you did while working on In a Snap: rather than design a query that takes advantage of existing indexes, your task is to design indexes which existing queries can take advantage of.

- <details><summary>Use <code>EXPLAIN QUERY PLAN</code> on each <code>SELECT</code> query to assess where best to create indexes</summary>

    ---
    Begin by assessing where best to create indexes by understanding the plan for each typical query on my.harvard’s database.

    For example, try revealing the plan for the first typical query, as by executing the following:

    ```sql
    EXPLAIN QUERY PLAN
    SELECT "courses"."title", "courses"."semester"
    FROM "enrollments"
    JOIN "courses" ON "enrollments"."course_id" = "courses"."id"
    JOIN "students" ON "enrollments"."student_id" = "students"."id"
    WHERE "students"."id" = 3;
    ```
    
    The output of the above is as follows:
    ```bash
    QUERY PLAN
    |--SEARCH students USING INTEGER PRIMARY KEY (rowid=?)
    |--SCAN enrollments
    `--SEARCH courses USING INTEGER PRIMARY KEY (rowid=?)
    ```

    Notice that, while the database engine is already `SEARCH`ing the students and courses tables using their primary key indexes, there are still improvements to be made: the database engine is `SCAN`ning the enrollments table without an index. Recall that to `SCAN` means that the database engine must search through all rows, one by one—a process that is much slower than searching an index!

    Experiment now by creating an index which could turn that SCAN into a SEARCH that uses an index. Then, repeat the same process for each of the typical queries on my.harvard’s database until you’ve arrived at a set of indexes which ensure all queries are using indexes to their full potential.

    </details>

- <details><summary>Minimize the number of indexes you've created</summary>

    ---
    Keep in mind that indexes take up additional space, and that they can slow `INSERT`, `UPDATE`, and `DELETE` queries. Once you’ve arrived at an initial set of indexes, start paring them down until you’ve created the minimum required for each query to use indexes optimally. How to start this process? Consider the following questions:

    - Do any of your indexes include the same columns? If so, it’s likely you need only one index on that particular column.
    - Do any of your indexes include columns unused by the given queries? If so, it’s likely you can remove those columns from your indexes.
    - Does removing an index have any impact on each query’s plan? If not, might be best to remove it!
    </details>

⚠️ Be sure to balance speed with disk space, only creating indexes you need.

</details>




### 🎯 Solution

| Indexed Tables  | Commit
|-----|------|
| enrollments, courses and satisfies | [0086e00](https://github.com/lucasOlivein/CS50-Harvard/commit/0086e001103b8390684d98a451b34d935b766f87)

### 📚 Source
_your.harvard_ from Harvard’s CS50 SQL course:https://cs50.harvard.edu/sql/psets/5/your.harvard/

### 📂 Download
Distribution code: https://cdn.cs50.net/sql/2024/x/psets/5/harvard.zip
