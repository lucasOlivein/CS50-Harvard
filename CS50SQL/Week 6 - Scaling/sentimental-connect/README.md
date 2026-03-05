# Happy to Connect (Sentimental)

### 🚀 Summary
...
### 📄 Description (Adapted)
...

### ⚙️ Specification
📌 **Task**: _In a file called `schema.sql` in a folder called `sentimental-connect`, write a set of SQL statements to design a **MySQL database** schema that LinkedIn could use._



<details><summary>📋 <strong>Requirements</strong></summary>

---
⭐ The implementation details are up to you, though you should minimally ensure that your database meets the **platform’s specification** and that it can represent the given **sample data**.

- <details><summary><strong> ⬜ Platform’s Specification</strong></summary>

    ---

    - <details><summary><strong> ⬜ Users</strong></summary>

        ---

        _The heart of LinkedIn’s platform is its people. Your database should be able to represent the following information about LinkedIn’s users:_

        - Their **first** and **last** name
        - Their **username**
        - Their **password**

        Keep in mind that, if a company is following best practices, application passwords are “[hashed](https://en.wikipedia.org/wiki/Hash_function)”.   
        No need to worry about hashing passwords here, though it might be helpful to know that some hashing algorithms can produce strings up to 128 characters long. .

        </details>

    - <details><summary><strong> ⬜ Schools and Universities</strong></summary>

        ---

        _LinkedIn also allows for official school or university accounts, such as [that for Harvard](https://www.linkedin.com/school/harvard-university/), so alumni (i.e., those who’ve attended) can identify their affiliation. Ensure that LinkedIn’s database can store the following information about each school:_

        - The **name of the school**
        - The **type of school**
        - The **school’s location**
        - The **year in which the school was founded**

        You should assume that LinkedIn only allows schools to choose one of three types: “Primary,” “Secondary,” and “Higher Education.”

        </details>

    - <details><summary><strong> ⬜ Companies</strong></summary>

        ---

        _LinkedIn allows companies to create their own pages, like the [one for LinkedIn itself](https://www.linkedin.com/company/linkedin/), so employees can identify their past or current employment with the company. Ensure that LinkedIn’s database can store the following information for each company:_

        - The name of the company
        - The company’s industry
        - The company’s location

        You should assume that LinkedIn only allows companies to choose from one of three industries: “Technology,” “Education,” and “Business.”

        </details>

    - <details><summary><strong> ⬜ Connections</strong></summary>

        ---

        _And finally, the essence of LinkedIn is its ability to facilitate connections between people. Ensure LinkedIn’s database can support each of the following connections._

        - <details><summary> ⬜ <strong>Connections with People</strong></summary>
        
            ---

            _LinkedIn’s database should be able to represent mutual (reciprocal, two-way) connections between users. No need to worry about one-way connections, such as user A “following” user B without user B “following” user A._
            </details>

        - <details><summary> ⬜ <strong>Connections with Schools</strong></summary>
        
            ---

            _A user should be able to create an affiliation with a given school. And similarly, that school should be able to find its alumni. Additionally, allow a user to define:_

            - The start date of their affiliation (i.e., when they started to attend the school)
            - The end date of their affiliation (i.e., when they graduated), if applicable
            - The type of degree earned/pursued (e.g., “BA”, “MA”, “PhD”, etc.)



            </details>

        - <details><summary>⬜ <strong>Connections with Companies</strong></summary>
        
            ---


            _A user should be able to create an affiliation with a given company. And similarly, a company should be able to find its current and past employees. Additionally, allow a user to define:_

            - The start date of their affiliation (i.e., the date they began work with the company)
            - The end date of their affiliation (i.e., when left the company), if applicable
    
            </details>
        
        </details>
    </details>


- <details><summary><strong> ⬜ Sample Data</strong></summary>

    ---

    _Your database should be able to represent:_

    - A user, [Claudine Gay](https://en.wikipedia.org/wiki/Claudine_Gay), whose username is “claudine” and password is “password”.
    - A user, [Reid Hoffman](https://en.wikipedia.org/wiki/Reid_Hoffman) whose username is “reid” and password is “password”.
    - A school, **Harvard University**, which is a university located in Cambridge, Massachusetts, founded in 1636.
    - A company, **LinkedIn**, which is a technology company headquartered in Sunnyvale, California.
    - Claudine Gay’s **connection with Harvard**, pursuing a PhD from January 1st, 1993, to December 31st, 1998.
    - Reid Hoffman’s **connection with LinkedIn**, with title “CEO and Chairman”, from January 1st, 2003 to February 1st, 2007


    </details>


</details>

<details><summary>📖 <strong>Advice</strong></summary>

---
- Consider the full range of MySQL’s supported types, which are documented in the MySQL 8.0 reference manual at [dev.mysql.com/doc/refman/8.0/en/data-types.html](https://dev.mysql.com/doc/refman/8.0/en/data-types.html).
- Also consider the reference manual’s advice on choosing the right type for a column, documented at [d]ev.mysql.com/doc/refman/8.0/en/choosing-types.html](https://dev.mysql.com/doc/refman/8.0/en/choosing-types.html).

    - Among the high-level pieces of advice is to choose the most precise type for your use case.   
    For instance, if you know an integer column will store only positive values, you should consider modifying the integer type with `UNSIGNED` (e.g., INT `UNSIGNED` or TINYINT `UNSIGNED`) to get the most range out of your type.

</details>


### 🎯 Solution
...

### 📚 Source
Based on the *Happy to Connect (Sentimental)* problem from Harvard’s CS50 SQL course: https://cs50.harvard.edu/sql/psets/6/connect/