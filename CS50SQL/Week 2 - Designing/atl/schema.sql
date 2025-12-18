CREATE TABLE "passengers" (
    "id" INTEGER PRIMARY KEY,
    "first_name" TEXT,
    "last_name" TEXT,
    "age" INTEGER
);

CREATE TABLE "airlines" (
    "id" INTEGER PRIMARY KEY,
    "name" TEXT NOT NULL,
    "concourse" TEXT NOT NULL
);

CREATE TABLE "flights" (
    "id" INTEGER PRIMARY KEY,
    "flight_number" INTEGER,
    "airline" INTEGER,
    "departure_airport_code" TEXT NOT NULL,
    "arrival_airport_code" TEXT NOT NULL,
    "expected_departure" TEXT NOT NULL,
    "expected_arrival" TEXT NOT NULL,
    FOREIGN KEY("airline") REFERENCES "airlines"("id")
);

CREATE TABLE "check-in" (
    "id" INTEGER PRIMARY KEY,
    "passenger_id" INTEGER,
    "flight_id" INTEGER,
    "datetime" TEXT NOT NULL,
    FOREIGN KEY("passenger_id") REFERENCES "passengers"("id"),
    FOREIGN KEY("flight_id") REFERENCES "flights"("id")
);