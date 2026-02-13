-- Task: write a SQL statement to create a view named one_bedrooms. 
-- This view should contain all listings that have exactly one bedroom. 
-- Ensure the view contains the following columns:
--   - id
--   - property_type
--   - host_name
--   - accomodates

-- listinings columns:
--  - id
--  - property_type
--  - host_name
--  - accommodates
--  - bedrooms
--  - descriptions

-- Answer:
CREATE VIEW "one_bedrooms" AS
SELECT "id", "property_type", "host_name", "accommodates"
FROM "listings"
WHERE "bedrooms" = 1;
