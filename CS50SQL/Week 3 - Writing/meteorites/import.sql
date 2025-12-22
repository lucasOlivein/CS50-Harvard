-- Temporary table used to stage and clean raw meteorite data
CREATE TABLE meteorites_temp (
    name TEXT,
    id INTEGER,
    nametype TEXT,
    class TEXT,
    mass REAL,
    discovery TEXT,
    year INTEGER,
    lat REAL,
    long REAL
);

-- Load raw meteorite CSV data (skip header) into the staging table
.import --csv --skip 1 meteorites.csv meteorites_temp

-- Data cleaning: convert to NULL empty values
-- Columns: mass, year, lat, long
UPDATE "meteorites_temp"
SET "mass" = NULL
WHERE "mass" = '';

UPDATE "meteorites_temp"
SET "year" = NULL
WHERE "year" = '';

UPDATE "meteorites_temp"
SET "lat" = NULL
WHERE "lat" = '';

UPDATE "meteorites_temp"
SET "long" = NULL
WHERE "long" = '';

-- Data cleaning: round to 2 decimal places
-- Columns: mass, lat, long
UPDATE "meteorites_temp"
SET "mass" = ROUND("mass", 2);

UPDATE "meteorites_temp"
SET "lat" = ROUND("lat", 2);

UPDATE "meteorites_temp"
SET "long" = ROUND("long", 2);

-- Data cleaning: exclude 'Relict' entries
DELETE from "meteorites_temp"
WHERE "nametype" = 'Relict';

-- Final meteorites table
CREATE TABLE meteorites (
    "id" INTEGER PRIMARY KEY,
    "name" TEXT,
    "class" TEXT,
    "mass" REAL,
    "discovery" TEXT,
    "year" TEXT,
    "lat" REAL,
    "long" REAL
);

-- Load cleaned data from meteorites_temp into the final meteorites table
INSERT INTO meteorites("name", "class", "mass", "discovery", "year", "lat", "long")
SELECT "name", "class", "mass", "discovery", "year", "lat", "long"
FROM "meteorites_temp"
ORDER BY "year", "name";
