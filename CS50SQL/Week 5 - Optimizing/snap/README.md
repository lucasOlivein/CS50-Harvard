# In a Snap

### 🚀 Summary
...
### 📄 Description (Adapted)
...

### 🗃️ Schema
...

### ⚙️ Specification
📌 **Task**: In each corresponding `.sql` file, write a SQL query to implement the features described below. 

⭐ **Note**: Since speed is of the essence, you’ll need to also ensure your query uses the specified index. The best way to ensure a query is using an index to check the results of `EXPLAIN QUERY PLAN`.

<details><summary>💎 <strong>Advice</strong></summary>

---

- <details><summary>Use <code>EXPLAIN QUERY PLAN</code> to show a query's steps</summary>

    ---

    To check the results of EXPLAIN QUERY PLAN, you need simply prepend EXPLAIN QUERY PLAN to your query:

    ```sql
    EXPLAIN QUERY PLAN
    SELECT "username"
    FROM "users"
    WHERE "id" = 151;
    ```

    </details>

- <details><summary>Interpret the results of <code>EXPLAIN QUERY PLAN</code></summary>

    ---
    `EXPLAIN QUERY PLAN` displays the steps the SQLite database engine will take to execute a given SQL query. The output of EXPLAIN QUERY PLAN can indicate whether a query is utilizing an index.

    - If you see a step labeled as `USING INDEX`, it signifies that the query is leveraging an index in that step.
    - If you see a step labeled as `USING COVERING INDEX`, it indicates that the query is using a covering index in that step.
        - Recall that a covering index is a special type of index that includes all the columns needed for the query. This means the database can fulfill the query directly from the index without having to look up additional data in a table.

    - When you see a step labeled as `USING INTEGER PRIMARY KEY`, it implies that the query is utilizing the index on the primary key column, which is provided automatically by SQLite when the primary key is of the INTEGER type affinity. It is an efficient way to access rows directly if the query conditions involve a table’s primary key.


    <details><summary><strong>Example 1</strong></summary>

    ---
    ```bash
    QUERY PLAN
    `--SEARCH users USING INDEX search_users_by_last_login (last_login_date>?)
    ```
    Notice that this query can be executed in a single step, by searching the index `search_users_by_last_login`.

    </details>
    <details><summary><strong>Example 2</strong></summary>

    ---
    ```bash
    QUERY PLAN
    |--SEARCH messages USING COVERING INDEX search_messages_by_to_user_id (to_user_id=?)
    `--SCALAR SUBQUERY 1
    `--SEARCH users USING COVERING INDEX sqlite_autoindex_users_1 (username=?)
    ```
    
    Notice that this query requires two steps:
    1. The first searches the index search_messages_by_to_user_id.
    2. The second resolves a subquery by searching the index `sqlite_autoindex_users_1`.

    </details>
    <details><summary><strong>Example 3</strong></summary>

    ---
    ```bash
    QUERY PLAN
    |--SEARCH messages USING INDEX search_messages_by_from_user_id (from_user_id=?)
    |--SCALAR SUBQUERY 1
    |  `--SEARCH users USING COVERING INDEX sqlite_autoindex_users_1 (username=?)
    |--USE TEMP B-TREE FOR GROUP BY
    `--USE TEMP B-TREE FOR ORDER BY
    ```
    Notice that this query involves several steps, and that it uses indexes to accomplish most:
    1. The first step searches the index `search_messages_by_from_user_id`.
    2. The second step searches the index `sqlite_autoindex_users_1`.
    3. The final steps use temporary B-trees to group and order the results.
    
    </details>
    <details><summary><strong>Example 4</strong></summary>

    ---
    ```sql
    QUERY PLAN
    |--SEARCH users USING INTEGER PRIMARY KEY (rowid=?)
    `--SCALAR SUBQUERY 1
    |--SCAN messages USING COVERING INDEX search_messages_by_to_user_id
    `--USE TEMP B-TREE FOR ORDER BY
    ```

    Notice that this query involves several steps, and that it uses indexes to accomplish most:
    1. The first step searches an automatic primary key index.
    2. The second step scans rows using the index `search_messages_by_to_user_id`.
    3. The final step uses a temporary B-tree to order the results.
    </details>
    <details><summary><strong>Example 5</strong></summary>

    ---
    ```bash
    QUERY PLAN
    `--COMPOUND QUERY
    |--LEFT-MOST SUBQUERY
    |  |--SEARCH friends USING COVERING INDEX sqlite_autoindex_friends_1 (user_id=?)
    |  `--SCALAR SUBQUERY 1
    |     `--SEARCH users USING COVERING INDEX sqlite_autoindex_users_1 (username=?)
    `--INTERSECT USING TEMP B-TREE
        |--SEARCH friends USING COVERING INDEX sqlite_autoindex_friends_1 (user_id=?)
        `--SCALAR SUBQUERY 3
            `--SEARCH users USING COVERING INDEX sqlite_autoindex_users_1 (username=?)
    ```

    Notice that this query involves many steps, and that it uses indexes to accomplish most. See in particular that the index `sqlite_autoindex_friends_1` is frequently accessed.

    </details>
    



    </details>
</details>

<details><summary><strong>📋 Requirements</strong></summary>

---

- <details><summary>⬜ <code>1.sql</code>: The app’s user engagement team needs to identify active users</summary>

    ---

    Find all usernames of users who have logged in since 2024-01-01.

    Ensure your query uses the `search_users_by_last_login` index, which is defined as follows:
    ```sql
    CREATE INDEX "search_users_by_last_login"
    ON "users"("last_login_date");
    ```

    </details>

- <details><summary>⬜ <code>2.sql</code>: Users need to be prevented from re-opening a message that has expired</summary>

    ---

    Find when the message with ID 151 expires. You may use the message’s ID directly in your query.

    Ensure your query uses the index automatically created on the primary key column of the messages table.
    </details>


- <details><summary>⬜ <code>3.sql</code>: The app needs to rank a user’s “best friends,” similar to Snapchat’s “Friend Emojis” feature</summary>

    ---

    Find the user IDs of the top 3 users to whom `creativewisdom377` sends messages most frequently.     
    Order the user IDs by the number of messages `creativewisdom377` has sent to those users, most to least.

    Ensure your query uses the `search_messages_by_from_user_id` index, which is defined as follows:

    ```sql
    CREATE INDEX "search_messages_by_from_user_id"
    ON "messages"("from_user_id");
    ```

    </details>


- <details><summary>⬜ <code>4.sql</code>: The app needs to send users a summary of their engagement</summary>

    ---

    Find the username of the most popular user, defined as the user who has had the most messages sent to them.

    Ensure your query uses the `search_messages_by_to_user_id` index, which is defined as follows:

    ```sql
    CREATE INDEX "search_messages_by_to_user_id"
    ON "messages"("to_user_id");
    ```
    </details>


- <details><summary>⬜ <code>5.sql</code>: For any two users, the app needs to quickly show a list of the friends they have in common</summary>

    ---

    Given two usernames, `lovelytrust487` and `exceptionalinspiration482`, find the user IDs of their mutual friends.

    A mutual friend is a user that both `lovelytrust487` and `exceptionalinspiration482` count among their friends.

    Ensure your query uses the index automatically created on primary key columns of the friends table. 
    
    This index is called `sqlite_autoindex_friends_1`.
    </details>


</details>

### 🎯 Solution
...

### 📚 Source
_In a Snap_ from Harvard’s CS50 SQL course:https://cs50.harvard.edu/sql/psets/5/snap/

### 📂 Download
Distribution code: https://cdn.cs50.net/sql/2024/x/psets/5/snap.zip