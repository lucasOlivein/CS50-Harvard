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
