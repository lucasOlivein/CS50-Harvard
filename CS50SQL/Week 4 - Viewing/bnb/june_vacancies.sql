-- Task: write a SQL statement to create a view named june_vacancies.
-- This view should contain all listings and the number of days in June of 2023 that they remained vacant.
-- Ensure the view contains the following columns:
--  Column              Table    
--  - id                - listings
--  - property_type     - listings
--  - host_name         - listings
--  - days_vacant       - availabilities

-- listings columns   availabilities columns
--  - id                - id
--  - property_type     - listing_id
--  - host_name         - date
--  - accommodates      - available [TRUE | FALSE] (TEXT)
--  - bedrooms          - price
--  - descriptions

-- Answer:
CREATE VIEW june_vacancies AS
SELECT "listings"."id", "property_type", "host_name", COUNT("listing_id") AS "days_vacant"
FROM "listings"
JOIN "availabilities" ON "listings"."id" = "availabilities"."listing_id"
WHERE "available" = 'TRUE' AND "date" LIKE '2023-06-%'
GROUP BY "listing_id";
