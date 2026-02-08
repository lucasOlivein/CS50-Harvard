# Bed and Breakfast

### 🚀 Summary
...

### 📄 Description (Adapted)

<details><summary><strong>Introduction</strong></summary>

---
A Bed and Breakfast (“BnB” for short!) is a short-term place one might stay and pay the owner for the service, similar to a hotel. Over the past few years, [AirBnB](https://www.airbnb.com/) has allowed most anyone to rent out their place, whether it’s a home, a cute cottage, or even a treehouse.

---
</details>

You’re a data analyst for the City of Boston and you’re interested in discovering how the rise of AirBnB has changed the local tourist scene. You’ve even compiled a database, bnb.db, filled with data directly from AirBnB. In bnb.db, whip up a few views that will paint a clearer picture of AirBnB’s influence on the city of Boston.

### 🗃️ Schema

<svg id="mermaid-1770486867048" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="erDiagram" style="max-width: 375.4666748046875px;" viewBox="0 0 375.4666748046875 285" role="graphics-document document" aria-roledescription="er"><style>#mermaid-1770486867048{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-1770486867048 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-1770486867048 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-1770486867048 .error-icon{fill:#a44141;}#mermaid-1770486867048 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-1770486867048 .edge-thickness-normal{stroke-width:1px;}#mermaid-1770486867048 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-1770486867048 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-1770486867048 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-1770486867048 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-1770486867048 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-1770486867048 .marker{fill:lightgrey;stroke:lightgrey;}#mermaid-1770486867048 .marker.cross{stroke:lightgrey;}#mermaid-1770486867048 svg{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;}#mermaid-1770486867048 p{margin:0;}#mermaid-1770486867048 .entityBox{fill:#1f2020;stroke:#ccc;}#mermaid-1770486867048 .relationshipLabelBox{fill:hsl(20, 1.5873015873%, 12.3529411765%);opacity:0.7;background-color:hsl(20, 1.5873015873%, 12.3529411765%);}#mermaid-1770486867048 .relationshipLabelBox rect{opacity:0.5;}#mermaid-1770486867048 .labelBkg{background-color:rgba(32.0000000001, 31.3333333334, 31.0000000001, 0.5);}#mermaid-1770486867048 .edgeLabel .label{fill:#ccc;font-size:14px;}#mermaid-1770486867048 .label{font-family:"trebuchet ms",verdana,arial,sans-serif;color:#ccc;}#mermaid-1770486867048 .edge-pattern-dashed{stroke-dasharray:8,8;}#mermaid-1770486867048 .node rect,#mermaid-1770486867048 .node circle,#mermaid-1770486867048 .node ellipse,#mermaid-1770486867048 .node polygon{fill:#1f2020;stroke:#ccc;stroke-width:1px;}#mermaid-1770486867048 .relationshipLine{stroke:lightgrey;stroke-width:1;fill:none;}#mermaid-1770486867048 .marker{fill:none!important;stroke:lightgrey!important;stroke-width:1;}#mermaid-1770486867048 :root{--mermaid-font-family:"trebuchet ms",verdana,arial,sans-serif;}</style><g><defs><marker id="mermaid-1770486867048_er-onlyOneStart" class="marker onlyOne er" refX="0" refY="9" markerWidth="18" markerHeight="18" orient="auto"><path d="M9,0 L9,18 M15,0 L15,18"></path></marker></defs><defs><marker id="mermaid-1770486867048_er-onlyOneEnd" class="marker onlyOne er" refX="18" refY="9" markerWidth="18" markerHeight="18" orient="auto"><path d="M3,0 L3,18 M9,0 L9,18"></path></marker></defs><defs><marker id="mermaid-1770486867048_er-zeroOrOneStart" class="marker zeroOrOne er" refX="0" refY="9" markerWidth="30" markerHeight="18" orient="auto"><circle fill="white" cx="21" cy="9" r="6"></circle><path d="M9,0 L9,18"></path></marker></defs><defs><marker id="mermaid-1770486867048_er-zeroOrOneEnd" class="marker zeroOrOne er" refX="30" refY="9" markerWidth="30" markerHeight="18" orient="auto"><circle fill="white" cx="9" cy="9" r="6"></circle><path d="M21,0 L21,18"></path></marker></defs><defs><marker id="mermaid-1770486867048_er-oneOrMoreStart" class="marker oneOrMore er" refX="18" refY="18" markerWidth="45" markerHeight="36" orient="auto"><path d="M0,18 Q 18,0 36,18 Q 18,36 0,18 M42,9 L42,27"></path></marker></defs><defs><marker id="mermaid-1770486867048_er-oneOrMoreEnd" class="marker oneOrMore er" refX="27" refY="18" markerWidth="45" markerHeight="36" orient="auto"><path d="M3,9 L3,27 M9,18 Q27,0 45,18 Q27,36 9,18"></path></marker></defs><defs><marker id="mermaid-1770486867048_er-zeroOrMoreStart" class="marker zeroOrMore er" refX="18" refY="18" markerWidth="57" markerHeight="36" orient="auto"><circle fill="white" cx="48" cy="18" r="6"></circle><path d="M0,18 Q18,0 36,18 Q18,36 0,18"></path></marker></defs><defs><marker id="mermaid-1770486867048_er-zeroOrMoreEnd" class="marker zeroOrMore er" refX="39" refY="18" markerWidth="57" markerHeight="36" orient="auto"><circle fill="white" cx="9" cy="18" r="6"></circle><path d="M21,18 Q39,0 57,18 Q39,36 21,18"></path></marker></defs><g class="root"><g class="clusters"></g><g class="edgePaths"><path d="M132.867,87.04L120.389,96.283C107.911,105.526,82.956,124.013,70.478,141.673C58,159.333,58,176.167,58,184.583L58,193" id="id_entity-Listing-0_entity-Review-1_0" class="edge-thickness-normal edge-pattern-solid relationshipLine" style="undefined;;;undefined" data-edge="true" data-et="edge" data-id="id_entity-Listing-0_entity-Review-1_0" data-points="W3sieCI6MTMyLjg2NjY2NDg4NjQ3NDYsInkiOjg3LjAzOTUwOTMzNzQ1OTQ4fSx7IngiOjU4LCJ5IjoxNDIuNX0seyJ4Ijo1OCwieSI6MTkzfV0=" marker-start="url(#mermaid-1770486867048_er-onlyOneStart)" marker-end="url(#mermaid-1770486867048_er-zeroOrMoreEnd)"></path><path d="M232.867,87.04L245.344,96.283C257.822,105.526,282.778,124.013,295.256,141.673C307.733,159.333,307.733,176.167,307.733,184.583L307.733,193" id="id_entity-Listing-0_entity-Availability-2_1" class="edge-thickness-normal edge-pattern-solid relationshipLine" style="undefined;;;undefined" data-edge="true" data-et="edge" data-id="id_entity-Listing-0_entity-Availability-2_1" data-points="W3sieCI6MjMyLjg2NjY2NDg4NjQ3NDYsInkiOjg3LjAzOTUwOTMzNzQ1OTQ4fSx7IngiOjMwNy43MzMzMjk3NzI5NDkyLCJ5IjoxNDIuNX0seyJ4IjozMDcuNzMzMzI5NzcyOTQ5MiwieSI6MTkzfV0=" marker-start="url(#mermaid-1770486867048_er-onlyOneStart)" marker-end="url(#mermaid-1770486867048_er-oneOrMoreEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel" transform="translate(58, 142.5)"><g class="label" data-id="id_entity-Listing-0_entity-Review-1_0" transform="translate(-25.89167022705078, -10.5)"><foreignObject width="51.78334045410156" height="21"><div style="display: table-cell; white-space: nowrap; line-height: 1.5; max-width: 200px; text-align: center;" xmlns="http://www.w3.org/1999/xhtml" class="labelBkg"><span class="edgeLabel"><p>receives</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(307.7333297729492, 142.5)"><g class="label" data-id="id_entity-Listing-0_entity-Availability-2_1" transform="translate(-10.333335876464844, -10.5)"><foreignObject width="20.666671752929688" height="21"><div style="display: table-cell; white-space: nowrap; line-height: 1.5; max-width: 200px; text-align: center;" xmlns="http://www.w3.org/1999/xhtml" class="labelBkg"><span class="edgeLabel"><p>has</p></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="entity-Listing-0" transform="translate(182.8666648864746, 50)"><rect class="basic label-container" style="" x="-50" y="-42" width="100" height="84"></rect><g class="label" style="" transform="translate(-23.425003051757812, -12)"><rect></rect><foreignObject width="46.850006103515625" height="24"><div style="display: table-cell; white-space: nowrap; line-height: 1.5; max-width: 100px; text-align: center;" xmlns="http://www.w3.org/1999/xhtml"><span class="nodeLabel"><p>Listing</p></span></div></foreignObject></g></g><g class="node default" id="entity-Review-1" transform="translate(58, 235)"><rect class="basic label-container" style="" x="-50" y="-42" width="100" height="84"></rect><g class="label" style="" transform="translate(-25.21666717529297, -12)"><rect></rect><foreignObject width="50.43333435058594" height="24"><div style="display: table-cell; white-space: nowrap; line-height: 1.5; max-width: 100px; text-align: center;" xmlns="http://www.w3.org/1999/xhtml"><span class="nodeLabel"><p>Review</p></span></div></foreignObject></g></g><g class="node default" id="entity-Availability-2" transform="translate(307.7333297729492, 235)"><rect class="basic label-container" style="" x="-59.73332977294922" y="-42" width="119.46665954589844" height="84"></rect><g class="label" style="" transform="translate(-39.73332977294922, -12)"><rect></rect><foreignObject width="79.46665954589844" height="24"><div style="display: table-cell; white-space: nowrap; line-height: 1.5; max-width: 200px; text-align: center;" xmlns="http://www.w3.org/1999/xhtml"><span class="nodeLabel"><p>Availability</p></span></div></foreignObject></g></g></g></g></g></svg>

Within `bnb.db`, you’ll find three tables that implement the relationships described in the ER diagram above.

<details><summary><strong>listings</strong></summary>

--- 

The `listings` table contains the following columns:

- `id`, which is the ID of the listing.
- property_type, which is the type of the listing (e.g., “Entire - rental unit”, “Private room in rental unit”, etc.).
- `host_name`, which is the AirBnB username of the listing’s host.
- `accommodates`, which is the listing’s maximum number of occupants.
- `bedrooms`, which is the listing’s number of bedrooms.
- `description`, which is the description of the listing on AirBnB.

---
</details>

<details><summary><strong>reviews</strong></summary>

---

The `reviews` table contains the following columns:

- id`, which is the ID of the review.
- `listing_id`, which is the ID of the listing which received the review.
- `date`, which is the date the review was posted.
- `reviewer_name`, which is the AirBnB username of the reviewer.
- `comments`, which is the content of the review.

---

</details>

<details><summary><strong>availabilities</strong></summary>

---

availabilities table

The availabilities table contains the following columns:

- `id`, which is the id of the availability.
- `listing_id`, which is the listing ID associated with the availability.
- `date`, which is the date of the availability.
- `available`, which is whether the date is still available to be booked (TRUE or FALSE).
- `price`, which is the price of staying on the given date.


---
</details>

### ⚙️ Specification
📌 **Task**: In each of the corresponding `.sql` files, write a SQL statement to create each of the following views of the data in `bnb.db`. 

⭐ **Note**: while views can be created from other views, each of your views should stand alone (i.e., not rely on a prior view).

<details><summary><strong>📋 Requirements</strong></summary>

---

-  <details><summary><strong>⬜ No Descriptions</strong></summary>

    ---
    You might notice that when running
    ```sql
    SELECT * FROM "listings" LIMIT 5;
    ```

    the results look quite wonky! The description column contains descriptions with many line breaks, each of which are printed to your terminal.

    In `no_descriptions.sql`, write a SQL statement to create a view named `no_descriptions` that includes all of the columns in the listings table except for description.

    ---

    </details>

- <details><summary><strong>⬜ One-Bedrooms</strong></summary>

    ---

    In `one_bedrooms.sql`, write a SQL statement to create a view named `one_bedrooms`. 
    
    This view should contain all listings that have exactly one bedroom. 
    
    Ensure the view contains the following columns:

    - `id`, which is the id of the listing from the listings table.
    - `property_type`, from the listings table.
    - `host_name`, from the listings table.
    - `accommodates`, from the listings table.

    ---
    </details>

- <details><summary><strong>⬜ Available</strong></summary>

    --- 
    In `available.sql`, write a SQL statement to create a view named `available`. 
    
    This view should contain all dates that are available at all listings. 
    
    Ensure the view contains the following columns:

    - `id`, which is the id of the listing from the listings table.
    - `property_type`, from the listings table.
    - `host_name`, from the listings table.
    - `date`, from the availabilities table, which is the date of the availability.

    ---
    </details>

- <details><summary><strong>⬜ Frequently Reviewed</strong></summary>

    ---
    In `frequently_reviewed.sql`, write a SQL statement to create a view named `frequently_reviewed`. 
    
    This view should contain the 100 most frequently reviewed listings, sorted from most- to least-frequently reviewed. 
    
    Ensure the view contains the following columns:

    - `id`, which is the id of the listing from the listings table.
    - `property_type`, from the listings table.
    - `host_name`, from the listings table.
    - `reviews`, which is the number of reviews the listing has received.

    If any two listings have the same number of reviews, sort by `property_type` (in alphabetical order), followed by `host_name` (in alphabetical order).
    ---
    </details>

- <details><summary><strong>⬜ June Vacancies</strong></summary>

    ---

    In `june_vacancies.sql`, write a SQL statement to create a view named `june_vacancies`. 
    
    This view should contain all listings and the number of days in June of 2023 that they remained vacant. 
    
    Ensure the view contains the following columns:

    `id`, which is the id of the listing from the listings table.
    `property_type`, from the listings table.
    `host_name`, from the listings table.
    `days_vacant`, which is the number of days in June of 2023, that the given listing was marked as available.

    ---
    </details>

---
</details>


### 🎯 Solution
...

### 📚 Source
_Bed and Breakfast_ from Harvard’s CS50 SQL course: https://cs50.harvard.edu/sql/psets/4/bnb/

### 📂 Download
Distribution code: https://cdn.cs50.net/sql/2024/x/psets/4/bnb.zip