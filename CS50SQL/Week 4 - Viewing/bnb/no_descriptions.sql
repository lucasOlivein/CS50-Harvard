-- Task: write a SQL statement to create a view named no_descriptions that includes all of 
-- the columns in the listings table except for description.

-- listinings columns:
--  - id
--  - property_type
--  - host_name
--  - accommodates
--  - bedrooms
--  - descriptions

-- Answer:
CREATE VIEW "no_descriptions" AS
SELECT "id", "property_type", "host_name", "accommodates", "bedrooms"
FROM "listings";