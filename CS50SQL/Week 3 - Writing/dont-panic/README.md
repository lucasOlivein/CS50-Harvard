# Don't Panic!

### 🚀 Summary
...
### 📄 Description (Adapted)
...
### ⚙️ Specification
📌 **Task**: _In `hack.sql`, write a sequence of SQL statements to achieve the following:_

-  **Alter** the password of the website’s administrative account, admin, to instead be “oops!”.
- **Erase** any logs of the above password change recorded by the database.
-  **Add** false data to throw others off your trail. In particular, to frame `emily33`, make it only appear—in the `user_logs` table—as if the `admin` account has had its password changed to `emily33`’s password.

_When your SQL statements in `hack.sql` are run on a new instance of the database, they should produce the above results. Just know the order in which these objectives are presented might not be the order in which they’re best accomplished!_

_Also keep in mind that passwords are usually not stored “in the clear”—that is, as the plain characters that make up the password. Instead they’re “hashed,” or scrambled, to preserve privacy. Given this reality, you’ll need to ensure the password to which you change the administrative password is also hashed. Thankfully, you know that the passwords in the users table are already stored as [MD5 hashes](https://en.wikipedia.org/wiki/Cryptographic_hash_function). You can generate quickly generate such hashes from plaintext at [md5hashgenerator.com](https://www.md5hashgenerator.com/)._

<details><summary><strong>Hints</strong></summary>

---
- Recall you can `INSERT` into a table the rows returned by a SELECT statement, so long as the number of columns matches.
- You can create a subquery at any point in a SQL statement, not just as part of a `WHERE` clause.   
For instance, consider the following SQL query on a simplified `user_logs` table: 
```sql
INSERT INTO "user_logs" ("type", "password")
SELECT 'update', (
    SELECT "password"
    FROM "users"
    WHERE "username" = 'carter'
);
```
The above query will insert a new row into the `user_logs` table. The column type will have the value “update” and the column `password` will have the current password of the user `carter`.

---
</details>

### 🎯 Solution
...

### 📚 Source
_Don't Panic!_ from Harvard’s CS50 SQL course: https://cs50.harvard.edu/sql/psets/3/dont-panic/

### 📂 Download
Distribution code: https://cdn.cs50.net/sql/2024/x/psets/3/dont-panic.zip