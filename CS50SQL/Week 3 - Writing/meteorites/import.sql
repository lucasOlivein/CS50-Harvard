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
