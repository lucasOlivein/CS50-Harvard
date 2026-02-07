# 📊  Census Taker

### 🚀 Summary
...
### 📄 Description (Adapted)
...

### 🗃️ Schema
...

### ⚙️ Specification
📌 **Task**: In each of the corresponding `.sql` files, write a SQL statement to create each of the following views of the data in `census.db`. 

⭐ **Note**: while views can be created from other views, each of your views should stand alone (i.e., not rely on a prior view).

<details><summary><strong>📋 Requirements</strong></summary>


- <details><summary><strong>⬜ Rural</strong></summary>

    --- 
    
    This view should contain all census records relating to a rural municipality (identified by including “rural” in their name). 
    
    Ensure the view contains all of the columns from the `census` table.

    ---

    </details>

- <details><summary><strong>⬜ Total</strong></summary>

    ---

    In `total.sql`, write a SQL statement to create a view named `total`. 
    
    This view should contain the sums for each numeric column in census, across all districts and localities. 
    
    Ensure the view contains each of the following columns:

    - `families`, which is the sum of families from every locality in Nepal.
    - `households`, which is the sum of households from every locality in Nepal.
    - `population`, which is the sum of the population from every locality in Nepal.
    - `male`, which is the sum of people identifying as male from every locality in Nepal.
    - `female`, which is the sum of people identifying as female from every locality in Nepal.
    ---

    </details>

- <details><summary><strong>⬜ By District</strong></summary>

    ---

    In `by_district.sql`, write a SQL statement to create a view named `by_district`. 

    This view should contain the sums for each numeric column in census, grouped by district. 

    Ensure the view contains each of the following columns:

    - `district`, which is the name of the district.
    - `families`, which is the total number of families in the district.
    - `households`, which is the total number of households in the district.
    - `population`, which is the total population of the district.
    - `male`, which is the total number of people identifying as male in the district.
    - `female`, which is the total number of people identifying as female in the district.

    ---
    </details>


- <details><summary><strong>⬜ Most Populated</strong></summary>

    ---
    In `most_populated.sql`, write a SQL statement to create a view named `most_populated`. 
    
    This view should contain, in order from greatest to least, the most populated districts in Nepal. 
    
    Ensure the view contains each of the following columns:

    - `district`, which is the name of the district.
    - `families`, which is the total number of families in the district.
    - `households`, which is the total number of households in the district.
    - `population`, which is the total population of the district.
    - `male`, which is the total number of people identifying as male in the district.
    - `female`, which is the total number of people identifying as female in the district.

    ---
    </details>

</details>

### 🎯 Solution
...
### 📚 Source
_Census Taker_ from Harvard’s CS50 SQL course: https://cs50.harvard.edu/sql/psets/4/census/

### 📂 Download
Distribution code: https://cdn.cs50.net/sql/2024/x/psets/4/census.zip