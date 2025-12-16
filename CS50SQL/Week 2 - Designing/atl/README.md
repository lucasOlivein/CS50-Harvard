# ATL

### 🚀 Summary
...
### 📄 Description (Adapted)
...
### ⚙️ Specification

📌 **Task**: _In a file called `schema.sql` in a folder called `atl`, write a set of SQL statements to design a database with which Hartsfield-Jackson could keep track of its passengers and their flights._

<details><summary><strong>📋 Requirements</strong></summary>

<br>

_The implementation details are up to you, though you should minimally ensure your database meets this requirements and that it can represent the given sample data._

- <details><summary><strong> Passengers</strong></summary>

    <br>

    _When it comes to our passengers, we just need to have the essentials in line:_
    - **first name**, 
    - **last name**, and 
    - **age**
    
    _That’s all we need to know—nothing more._

    ---

    </details>
- <details><summary><strong>Check-Ins</strong></summary>

    <br>
    

    _When passengers arrive at ATL, they’ll often “check in” to their flights. That’s them telling us they’re here and all set to board.  
    We’d like to keep a tidy log of such moments. And what would we need to log, you ask? Well, here’s what we need:_

    - The exact **date and time** at which our passenger _checked in_
    - **The flight** they are checking in for, of course.   
    Can’t lose track of where they’re headed, now can we?


    --- 
    </details>
- <details><summary><strong>Airlines</strong></summary>

    <br>
    
    _ATL’s a hub for many [domestic and international airlines](https://en.wikipedia.org/wiki/Hartsfield%E2%80%93Jackson_Atlanta_International_Airport#Airlines_and_destinations): names like Delta, British Airways, Air France, Korean Air, and Turkish Airlines. The list goes on. So here’s what we track:_

    - The name of the airline
    - The “[concourse](https://en.wikipedia.org/wiki/Hartsfield%E2%80%93Jackson_Atlanta_International_Airport#Terminals)” or, shall I say, **the section of our airport** where the airline operates.   
    We have 7 concourses: 
        - **A**, **B**, **C**, **D**, **E**, **F**, and **T**.

    ---

    </details>
- <details><summary><strong>Flights</strong></summary>
    
    <br>
    
    _We serve as many as 1,000 flights daily. To ensure that our passengers are never left wondering, we need to give them all the critical details about their flight. Here’s what we’d like to store:_

    
    - **The flight number**. For example, “900”. Just know that we sometimes re-use flight numbers.
    - **The airline operating the flight**. You can keep it simple and assume one flight is operated by one airline.
    - **The code of the airport they’re departing from**. For example, “ATL” or “BOS”.
    - **The code of the airport they’re heading to**
    - **The expected departure date and time** (to the minute, of course!)
    - **The expected arrival date and time**, to the very same accuracy

    ---
    </details>


<details><summary><strong>Sample Data</strong></summary>

<br>

Your database should be able to represent:

- A passenger, **Amelia Earhart**, who is 39 years old
- An airline, **Delta**, which operates out of concourses A, B, C, D, and T
- A flight, **Delta Flight 300**, which is expected to depart from ATL on August 3rd, 2023 at 6:46 PM and arrive at BOS on August 3rd, 2023 at 9:09 PM
- A **check-in** for Amelia Earhart, for Delta Flight 300, on August 3rd, 2023 at 3:03 PM

---

</details>

</details>


### 🎯 Solution
...
### 📚 Source
Based on the *ATL* problem from Harvard’s CS50 SQL course: https://cs50.harvard.edu/sql/psets/2/atl/