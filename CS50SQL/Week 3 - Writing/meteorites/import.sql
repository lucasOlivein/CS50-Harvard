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
