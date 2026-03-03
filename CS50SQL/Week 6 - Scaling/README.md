# 🗓 Week 6 - Scaling

📌**Problem Set 6**: _Submit the problems bellow._

## 📝 Problems
- ⬜ Happy to Connect (Sentimental)
- ⬜ From the Deep
- ⬜ One of the following: 
    - ⬜ Don’t Panic! (Sentimental) with Python
    - ⬜ Don’t Panic! (Sentimental) with Java
## 🏷️ Topics

<details><summary><strong> 🔹 MySQL</strong></summary>

---

MySQL is the world's most popular open-source relational database management system (RDBMS).

It supports multi-user access, data security features, and scalability, making it a popular choice for applications ranging from small websites to large-scale platforms.


- <details><summary><strong>Basic Commands</strong></summary>

    ---

    -  <details><summary><strong>Connecting to the SQL server</strong></summary>

        ---
        ```bash
        mysql -u root -h 127.0.0.1 -P 3306 -p
        ```
        - In this terminal command, `-u` indicates the user. We provide the user we want to connect to the database as — `root` (synonymous with database admin, in this case).
        - `127.0.0.1` is the address of local host on the internet (our own computer).
        - `3306` is the port we want to connect to, and this is the default port where MySQL is hosted. Think of the combination of host and port as the address of the database we are trying to connect to!
        -  `-p `at the end of the command indicates that we want to be prompted for a password when connecting.

        </details>

    -  <details><summary><strong>Database Commands</strong></summary>

        ---

        To show all the existing databases inside the database server, we use the following MySQL command. 
        ```sql
        SHOW DATABASE;
        ```

        Creating a new database:
        ```sql
        CREATE DATABASE `mbta`;
        ```

        To change the current database to mbta:
        ```sql
        USE `mbta`;
        ```

        To drop the database:
        ```sql
        DROP DATABASE `mbta`;
        ```
        </details>


    - <details><summary><strong>Table Commands</strong></summary>

        ---

        - Let us now create the table cards using an `INT` data type for the `ID` column.
            ```sql
            CREATE TABLE `cards` (
                `id` INT AUTO_INCREMENT,
                PRIMARY KEY(`id`)
            );
            ```

        - After creating the table, we can see a list of the existing tables by running:
            ```sql
            SHOW TABLES;
            ```

        - For further details about a table, we can use the `DESCRIBE` command.
            ```sql
            DESCRIBE `cards`;
            ```

        - To rename the table:
            ```sql
            RENAME TABLE `cards` TO `Ccard`;
            ```

        - To drop the table:
            ```sql
            DROP TABLE `Ccard`; 
            ```
        </details>

    - <details><summary><strong>Data Manipulation (DML)</strong></summary>

        ---

        - ```sql
            SELECT * FROM table;    
            ```

        - ```sql    
            INSERT INTO table VALUES (...); 
            ```

        - ```sql
            UPDATE table SET column=value WHERE ...; 
            ```


        - ```sql
            DELETE FROM table WHERE ...;     
            ```

        </details>

    - <details><summary><strong>Modify Table Structure (ALTER)</strong></summary>

        ---

        - ```sql
            ALTER TABLE table ADD column_name datatype;
            ```

        
        - ```sql
            ALTER TABLE table MODIFY column_name datatype;
            ```
        
        - ```sql
            ALTER TABLE table DROP column;
            ```
        
        
        </details>
    
    - <details><summary><strong>Users and Permissions</strong></summary>

        ---

        - ```sql
            CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
            ```

        - ```sql
            GRANT ALL PRIVILEGES ON database.* TO 'user'@'localhost';
            ```
        
        - ```sql
            REVOKE ALL PRIVILEGES ON database.* FROM 'user'@'localhost';
            ```

        - ```sql
            DROP USER 'user'@'localhost';
            ```

        - ```sql
            FLUSH PRIVILEGES;
            ```

        </details>
    
    - <details><summary><strong>Useful System Commands</strong></summary>

        ---

        - ```sql
            SELECT VERSION();
            ```

        - ```sql
            EXIT;
            ``` 
        </details>

    </details>

- <details><summary><strong>Data Types</strong></summary>

    ---
    - <details><summary><strong>Numeric</strong></summary>

        ---
        - <details><summary><strong>Integer</strong></summary>

            ---

            | Type | Size (bytes) | Minimum Value (signed) | Maximum Value (signed) | Maximum Value (unsigned)  |
            |------|:-------------:|:--------:|:-------:|:-------:|
            | `TINYINT` | 1  | -128  | 127  | 255 |
            | `SMALLINT` | 2  |  -32,768   | 32,767  | 65,535 |
            | `MEDIUMINT` | 3   |   -8,388,608    | 8,388,607 | 16,777,215 |
            | `INT` / `INTEGER` | 4  | -2,147,483,648 | 2,147,483,647 | $2^{32}$-1 |
            | `BIGINT`  |   8   | -$2^{63}$ | $2^{63}$-1 | $2^{64}$-1

            ✔ They can be **SIGNED** (negative and positive values) or **UNSIGNED** (positive only).

            </details>

        - <details><summary><strong>Fixed-Point and Floating-Point Types</strong></summary>

            ---

            | Type  |   |       |
            |-------|----|------|
            | `DECIMAL(M,D)` | 
            | `NUMERIC(M,D)` |
            | `FLOAT`       |
            |  `DOUBLE`      |

            </details>
        </details>

    - <details><summary><strong>Date and Time </strong></summary> 

        ---

        | Type | Description |   |
        |------|:----:|---|
        | `DATE`  |  Date (YYYY-MM-DD) |
        |  `TIME` | Time (HH:MM:SS) |
        |  `DATETIME`  | Date and time (YYYY-MM-DD HH:MM:SS) |
        |  `TIMESTAMP` | Date and time with automatic initialization/update (YYYY-MM-DD HH:MM:SS) |
        |  `YEAR`      | Year value (YYYY) |

        </details>

    - <details><summary><strong> 🔸 String </strong></summary>


        </details>
    

    - <details><summary><strong> 🔸 Boolean Type</strong></summary>


        </details>


    - <details><summary><strong> 🔸 ENUM and SET</strong></summary>


        </details>


    </details>


- <details><summary><strong>Stored Procedures</strong></summary>

    ---
    Stored procedures are a way to automate SQL statements and run them repeatedly.

    - <details><summary><strong>Basic structure:</strong></summary>

        ---

        - Example:
            ```sql
            DELIMITER //

            CREATE PROCEDURE procedure_name()
            BEGIN
                SELECT * FROM clientes;
            END //

            DELIMITER ;
            ```

        - To run:
            ```sql
            CALL procedure_name();
            ```

        </details>


    - <details><summary><strong>Stored Procedures with Parameters</strong></summary>

        ---

        - <details><summary><strong>IN Parameter</strong></summary>

            ---
            - `IN` is the default parameter type.
            - It is used to pass a value into the procedure.
            - The procedure can read it but cannot modify it (changes do not affect the caller).

            - Example:
                ```sql
                DELIMITER //

                CREATE PROCEDURE get_user_by_id(IN user_id INT)
                BEGIN
                    SELECT * FROM users WHERE id = user_id;
                END //

                DELIMITER ;
                ```
            - To run:

                ```sql
                CALL get_user_by_id(1);
                ```

            ✔ The value 1 is passed into the procedure.
            </details>

        - <details><summary><strong>OUT Parameter</strong></summary>

            ---

            - `OUT` is used to return a value from the procedure.
            - The caller must provide a variable to store the result.
            - The procedure assigns a value to that parameter.

            - Example:
                ```sql
                DELIMITER //

                CREATE PROCEDURE count_users(OUT total INT)
                BEGIN
                    SELECT COUNT(*) INTO total FROM users;
                END //

                DELIMITER ;
                ```
            
            - To run:
                ```sql
                CALL count_users(@total_users);
                SELECT @total_users;
                ```
            
            ✔ The procedure sets the value of `@total_users`.
            </details>

        - <details><summary><strong>INOUT Parameter</strong></summary>

            ---

            - `INOUT` works as both input and output.
            - You send an initial value to the procedure.
            - The procedure can modify it and return the new value.

            - Example:
                ```sql
                DELIMITER //

                CREATE PROCEDURE double_value(INOUT num INT)
                BEGIN
                    SET num = num * 2;
                END //

                DELIMITER ;
                ```
            
            - To run:
                ```sql
                SET @value = 5;
                CALL double_value(@value);
                SELECT @value;
                ```

            ✔ Initial value: `5`   
            ✔ Final value: `10`
            
            </details>


        </details>
    
    - <details><summary><strong>Control Flow Blocks</strong></summary>

        ---

        Stored procedures can be considerably improved in logic and complexity by using some regular old programming constructs. 

        - <details><summary><strong>IF / ELSE / ELSEIF</strong></summary>

            ---
            Conditional logic: 

            - ```sql
                DELIMITER //

                CREATE PROCEDURE check_number(IN num INT)
                BEGIN
                    IF num > 0 THEN
                        SELECT 'Positive number';
                    ELSEIF num < 0 THEN
                        SELECT 'Negative number';
                    ELSE
                        SELECT 'Zero';
                    END IF;
                END //

                DELIMITER ;
                ```

            </details>
        
        - <details><summary><strong>WHILE Loop</strong></summary>

            ---
            Executes while a condition is true.   
            Pre-condition loop:

            - ```sql
                DELIMITER //

                CREATE PROCEDURE while_example()
                BEGIN
                    DECLARE counter INT DEFAULT 1;

                    WHILE counter <= 5 DO
                        SELECT counter;
                        SET counter = counter + 1;
                    END WHILE;
                END //

                DELIMITER ;
                ```
            </details>

        - <details><summary><strong>REPEAT Loop</strong></summary>

            ---

            Executes at least once, stops when condition becomes true.    
            Post-condition loop:

            - ```sql
                DELIMITER //

                CREATE PROCEDURE repeat_example()
                BEGIN
                    DECLARE counter INT DEFAULT 1;

                    REPEAT
                        SELECT counter;
                        SET counter = counter + 1;
                    UNTIL counter > 5
                    END REPEAT;
                END //

                DELIMITER ;
                ```
            </details>

        - <details><summary><strong>LOOP (with LEAVE)</strong></summary>

            ---

            Generic loop that requires manual exit.  
            Infinite loop (manual exit), LEAVE ~ BREAK:
            - ```sql
                DELIMITER //

                CREATE PROCEDURE loop_example()
                BEGIN
                    DECLARE counter INT DEFAULT 1;

                    my_loop: LOOP
                        SELECT counter;
                        SET counter = counter + 1;

                        IF counter > 5 THEN
                            LEAVE my_loop;
                        END IF;
                    END LOOP my_loop;
                END //

                DELIMITER ;
                ```
            </details>
        
        - <details><summary><strong>Using ITERATE (continue behavior)</strong></summary>

            ---
            INTERATE ~ CONTINUE:

            - ```sql
                DELIMITER //

                CREATE PROCEDURE iterate_example()
                BEGIN
                    DECLARE counter INT DEFAULT 0;

                    my_loop: LOOP
                        SET counter = counter + 1;

                        IF counter = 3 THEN
                            ITERATE my_loop;
                        END IF;

                        SELECT counter;

                        IF counter >= 5 THEN
                            LEAVE my_loop;
                        END IF;
                    END LOOP my_loop;
                END //

                DELIMITER ;
                ```
            </details>
        
        </details>

- <details><summary><strong> 🔸 Access Controls</strong></summary>

    ---


    </details>

</details>




<details><summary><strong> 🔸 PostgreSQL</strong></summary>

---

...

</details>





<details><summary><strong> 🔸 SQL Injection Attacks</strong></summary>

---


</details>