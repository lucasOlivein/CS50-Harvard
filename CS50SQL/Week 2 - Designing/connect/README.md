# Happy to Connect

### 🚀 Summary
...
### 📄 Description (Adapted)
...
### ⚙️ Specification
📌 **Task**: _In a file called `schema.sql` in a folder called `connect`, write a set of SQL statements to design a database **LinkedIn** could use._

<details><summary>📋 <strong>Requirements:</strong></summary>

<br>

_The implementation details are up to you, though you should minimally ensure that your database meets the **platform’s specification** and that it can represent the given **sample data**._


<details><summary><strong> ⬜ Platform’s Specification</strong></summary>

<br>

- <details><summary><strong> ⬜ Users</strong></summary>

    <br>

    _The heart of LinkedIn’s platform is its people. Your database should be able to represent the following information about LinkedIn’s users:_

    - Their first and last name
    - Their username
    - Their password

    Keep in mind that, if a company is following best practices, application passwords are “[hashed](https://en.wikipedia.org/wiki/Hash_function)”.   
    No need to worry about hashing passwords here, though.

    ---
    </details>

- <details><summary><strong> ⬜ Schools and Universities</strong></summary>

    <br>

    _LinkedIn also allows for official school or university accounts, such as [that for Harvard](https://www.linkedin.com/school/harvard-university/), so alumni (i.e., those who’ve attended) can identify their affiliation. Ensure that LinkedIn’s database can store the following information about each school:_

    - The name of the school
    - The type of school (e.g., “Elementary School”, “Middle School”, “High School”, “Lower School”, “Upper School”, “College”, “University”, etc.)
    - The school’s location
    - The year in which the school was founded

    ---
    </details>

- <details><summary><strong> ⬜ Companies</strong></summary>

    <br>

    _LinkedIn allows companies to create their own pages, like the one for LinkedIn itself, so employees can identify their past or current employment with the company. Ensure that LinkedIn’s database can store the following information for each company:_

    - The name of the company
    - The company’s industry (e.g., “Education”, “Technology, “Finance”, etc.)
    - The company’s location

    ---
    </details>

- <details><summary><strong> ⬜ Connections</strong></summary>

    <br>

    _And finally, the essence of LinkedIn is its ability to facilitate connections between people. Ensure LinkedIn’s database can support each of the following connections._

    - <details><summary><strong>Connections with People</strong></summary>
    
        <br>

        _LinkedIn’s database should be able to represent mutual (reciprocal, two-way) connections between users. No need to worry about one-way connections, such as user A “following” user B without user B “following” user A._
        </details>

    - <details><summary><strong>Connections with Schools</strong></summary>
    
        <br>

        _A user should be able to create an affiliation with a given school. And similarly, that school should be able to find its alumni. Additionally, allow a user to define:_

        - The start date of their affiliation (i.e., when they started to attend the school)
        - The end date of their affiliation (i.e., when they graduated), if applicable
        - The type of degree earned/pursued (e.g., “BA”, “MA”, “PhD”, etc.)



        </details>

    - <details><summary><strong>Connections with Companies</strong></summary>
    
        <br>


        _A user should be able to create an affiliation with a given company. And similarly, a company should be able to find its current and past employees. Additionally, allow a user to define:_

        - The start date of their affiliation (i.e., the date they began work with the company)
        - The end date of their affiliation (i.e., when left the company), if applicable
        - The title they held while affiliated with the company


        </details>
    ---
    </details>
</details>

<details><summary><strong> ⬜ Sample Data</strong></summary>

<br>

_Your database should be able to represent:_

- A user, **[Alan Garber](https://en.wikipedia.org/wiki/Alan_Garber)**, whose username is “alan” and password is “password”.
- A user, **[Reid Hoffman](https://en.wikipedia.org/wiki/Reid_Hoffman)** whose username is “reid” and password is “password”.
- A school, **Harvard University**, which is a university located in Cambridge, Massachusetts, founded in 1636.
- A company, **LinkedIn**, which is a technology company headquartered in Sunnyvale, California.
- Alan Garber’s **undergraduate education at Harvard**, pursuing a BA from September 1st, 1973 to June 1st, 1976.
- Reid Hoffman’s **employment with LinkedIn** as its CEO and Chairman, from January 1st, 2003 to February 1st, 2007.


</details>

</details>


### 🎯 Solution
...
### 📚 Source
Based on the *Happy to Connect* problem from Harvard’s CS50 SQL course: https://cs50.harvard.edu/sql/psets/2/connect/