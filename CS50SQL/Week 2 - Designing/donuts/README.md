# Union Square Donuts

### 🚀 Summary
...
### 📄 Description (Adapted)
...
### ⚙️ Specification
📌 **Task**: _In a file called `schema.sql` in a folder called `donuts`, write a set of SQL statements to create a database that [Union Square Donuts](https://www.unionsquaredonuts.com/about) could use to manage their day-to-day operations._

<details><summary>📋 <strong>Requirements:</strong></summary>

<br>

_The implementation details are up to you, though you should minimally ensure that your database meets the team’s **expectations** and that it can represent the **sample data**._

<details><summary><strong> ⬜ Expectations</strong></summary>

<br>

_To understand the team’s expectations for their database, you sat down to talk with them after the shop closed for the day._

- <details><summary><strong>⬜ Ingredients</strong></summary>

    <br>

    _We certainly need to keep track of our ingredients. Some of the typical ingredients we use include flour, yeast, oil, butter, and several different types of sugar. Moreover, we would love to keep track of the price we pay per unit of ingredient (whether it’s pounds, grams, etc.)._ 
    </details>

- <details><summary><strong>⬜ Donuts</strong></summary>

    <br>

    _We’ll need to include our selection of donuts, past and present! For each donut on the menu, we’d love to include three things:_

    - The name of the donut
    - Whether the donut is [gluten-free](https://en.wikipedia.org/wiki/Gluten-free_diet)
    - The price per donut

    </details>

- <details><summary><strong>⬜ Orders</strong></summary>

    <br>
    
    _We love to see customers in person, though we realize a good number of people might order online nowadays. We’d love to be able to keep track of those online orders. We think we would need to store:_

    - An order number, to keep track of each order internally
    - All the donuts in the order
    - The customer who placed the order. We suppose we could assume only one customer places any given order.



    </details>

- <details><summary><strong>⬜ Customers</strong></summary>

    <br>

    _Oh, and we realize it would be lovely to keep track of some information about each of our customers. We’d love to remember the history of the orders they’ve made. In that case, we think we should store:_

    - A customer’s first and last name
    - A history of their orders


    </details>

</details>


<details><summary><strong> ⬜ Sample Data</strong></summary>

<br>

_Your database should be able to represent:_

- **Cocoa**, for which Union Square Donuts pays $5.00 for one pound.
- **Sugar**, for which Union Square Donuts pays $2.00 for one pound.
- Union Square Donuts’ **“Belgian Dark Chocolate” donut**, which is not gluten-free, costs $4.00, and includes the following ingredients:
    - Cocoa
    - Flour
    - Buttermilk
    - Sugar
- Union Square Donuts’ **“Back-To-School Sprinkles” donut**, which is not gluten-free, costs $4.00, and includes the following ingredients:
    - Flour
    - Buttermilk
    - Sugar
    - Sprinkles
- **Order 1** from **Luis Singh** for 3 Belgian Dark Chocolate donuts and 2 Back-To-School Sprinkles donuts.

</details>

</details>

### 🎯 Solution
| Feature | Commit |
|:----------|--------|
| `ingredients per donut` | [70c9d1f](https://github.com/lucasOlivein/CS50-Harvard/commit/70c9d1fbb68ebf0eea181d1800dc2382fab00b83)
| `donuts per order` | [da2c33b](https://github.com/lucasOlivein/CS50-Harvard/commit/da2c33bdf3b3a95c9803b322794d688ad0107ce4)
| `orders` | [21e393e](https://github.com/lucasOlivein/CS50-Harvard/commit/21e393e711715cb99a0cdd058e1b6f3701dacd4b)
| `customers` | [4ab04df](https://github.com/lucasOlivein/CS50-Harvard/commit/4ab04df8d31315cda6fe03c65d4c6b1a6d72118c)
| `donuts` | [70c2fd2](https://github.com/lucasOlivein/CS50-Harvard/commit/70c2fd245959f28df3453ffbd5b4cc2189e4cf4d)
| `ingredients` | [14465eb](https://github.com/lucasOlivein/CS50-Harvard/commit/14465eb5fd71b32d1df665d0aba9bc5330da2874)

**Sample data script**: [a8154e7](https://github.com/lucasOlivein/CS50-Harvard/commit/a8154e75f8f65886792bd48d67cbd6d64e35e23c)

### 📚 Source
Based on the *Union Square Donuts* problem from Harvard’s CS50 SQL course: https://cs50.harvard.edu/sql/psets/2/donuts/