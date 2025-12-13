-- *** The Lost Letter ***
-- Check the number of records in the `addresses` table
SELECT * FROM addresses;

-- Start: The Lost Letter
-- Query 1 (FAILED): Retrieve `addresses.id` for "2 Finnegan Street, uptown"
SELECT "id" FROM addresses
WHERE "address" = '2 Finnegan Street, uptown';

-- Query 2 (FAILED): Retrieve `addresses.id` for "Finnegan Street"
SELECT "id" FROM addresses
WHERE "address" = 'Finnegan Street';

-- Query 3 (FAILED): Retrieve `addresses.id` for addresses that contain "Finnegan"
SELECT * FROM addresses
WHERE address LIKE '%Finnegan%';

-- Query 4 (SUCCEEDED): Retrieve `addresses.id` for addresses beginning with "2"
-- Selected result (8): 854 | 2 Finnigan Street | Residential
SELECT * FROM addresses
WHERE address LIKE '2 %';

-- Query 4 (SUCCEEDED): Retrieve `addresses.id` for "900 Somerville Avenue"
-- Result: 432 | 900 Somerville Avenue | Residential
SELECT * FROM "addresses"
WHERE address = '900 Somerville Avenue';

-- Query 5 (FAILED): Retrieve `packages` with 
--                  `from_address_id` = "900 Somerville Avenue" and 
--                  `to_address_id` = "2 Finnigan Street"
-- NOTE: Address values used instead of IDs (error)
SELECT * FROM "packages"
WHERE "from_address_id" = '900 Somerville Avenue' AND "to_address_id" = '2 Finnigan Street';

-- Query 6 (FAILED): Retrieve `packages` with
--                  `from_address_id` = "900 Somerville Avenue" and
--                  `to_address_id` = "2 Finnegan Street"
-- The hypothesis was that the destination address was mistyped. This could not be confirmed.
-- NOTE: Address values used instead of IDs (error)
SELECT * FROM "packages"
WHERE "from_address_id" = '900 Somerville Avenue' AND "to_address_id" = '2 Finnegan Street';

-- Query 7 (FAILED): Retrieve `packages` with
--                   `from_address_id` = "900 Somerville Avenue"
-- NOTE: Address values used instead of IDs (error)
SELECT * FROM "packages"
WHERE "from_address_id" = '900 Somerville Avenue';

-- The last three queries were incorrect: I was searching for IDs using names.
-- CORRECT: "900 Somerville Avenue" is the `ID` 432 and
--          "2 Finnigan Street" is the `ID` 854
-- Query 8 (SUCCEEDED): Retrieve `packages` with
--                      `from_address_id` = 432 and
--                      `to_address_id` = 854
-- Result: 384 | Congratulatory letter | 432 | 854
SELECT * FROM "packages"
WHERE "from_address_id" = 432 AND "to_address_id" = 854;

-- Query 9 (SUCCEEDED): Retrieve `scans` for "package_id" = 384
-- Results: 
--  - 54 | 1 | 384 | 432 | Pick | 2023-07-11 19:33:55.241794
--  - 94 | 1 | 384 | 854 | Drop | 2023-07-11 23:07:04.432178
SELECT * FROM "scans"
WHERE "package_id" = 384;

-- Finish: The Lost Letter — The package was delivered on 2023-07-11 at 23:07:04.432178.

-- *** The Devious Delivery ***

-- *** The Forgotten Gift ***

