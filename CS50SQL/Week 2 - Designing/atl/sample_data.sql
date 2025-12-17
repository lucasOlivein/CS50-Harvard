INSERT INTO "passengers" ("first_name", "last_name", "age")
VALUES ('Amelia', 'Earhart', 39);

INSERT INTO "airlines" ("name", "concourse")
VALUES ('Delta', 'A, B, C, D, and T');

INSERT INTO "flights" ("flight_number", "airline", 
                        "departure_airport_code", "arrival_airport_code", 
                        "expected_departure", "expected_arrival")
VALUES (300, 'Delta Flight', 'ATL', 'BOS', 'August 3rd, 2023 at 6:46 PM', 'August 3rd, 2023 at 9:09 PM');

INSERT INTO "check-in" ("passenger_id", "datetime", "flight_id")
VALUES (
    (
        SELECT "id" 
        FROM "passengers"
        WHERE "first_name" = 'Amelia' AND "last_name" = 'Earhart'), 
    'August 3rd, 2023 at 3:03 PM', 
    (
        SELECT "id" FROM "flights"
        WHERE "flight_number" = 300 AND "airline" = 'Delta Flight'
    )
    );