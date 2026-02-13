-- Task:  write a SQL statement to create a view named available. 
-- This view should contain all dates that are available at all listings. 
-- Ensure the view contains the following columns:
--      column          table
--  - id                - listings
--  - property_type     - listings
--  - host_name         - listings
--  - date              - availabilities

-- listings columns   availabilities columns
--  - id                - id
--  - property_type     - listing_id
--  - host_name         - date
--  - accommodates      - available [TRUE | FALSE] (TEXT)
--  - bedrooms          - price
--  - descriptions

-- Answer:
CREATE VIEW "available" AS 
SELECT "listings"."id", "property_type", "host_name", "date"
FROM "availabilities"
JOIN "listings" ON "listings"."id" = "availabilities"."listing_id"
WHERE "availabilities"."available" = 'TRUE';
