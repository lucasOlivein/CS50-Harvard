-- Task: write a SQL statement to create a view named frequently_reviewed. 
-- This view should contain the 100 most frequently reviewed listings, 
-- sorted from most- to least-frequently reviewed. 
-- Ensure the view contains the following columns:
--  Column                  Table
--  - id                    - listings
--  - property_type         - listings
--  - host_name             - listings
--  - reviews               - reviews

-- If any two listings have the same number of reviews, sort by property_type (in alphabetical order), 
-- followed by host_name (in alphabetical order).

-- reviews table columns:
--  - id
--  - listing_id
--  - date
--  - reviewer_name
--  - comments

-- Answer:
CREATE VIEW frequently_reviewed AS
SELECT "listings"."id", "property_type", "host_name", COUNT("listing_id") AS "reviews"
FROM "listings"
JOIN "reviews" ON "reviews"."listing_id" = "listings"."id"
GROUP BY "listing_id"
ORDER BY "reviews" DESC, "property_type", "host_name"
LIMIT 100;