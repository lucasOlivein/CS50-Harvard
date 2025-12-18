-- The "users" table contains the following columns:
--  "id", "first_name", "last_name", "username", "password"
INSERT INTO "users" ("first_name", "last_name", "username", "password")
VALUES ('Alan', 'Garber', 'alan', 'password'),
    ('Reid', 'Hoffman', 'reid', 'password');

-- The "schools" table contains the following columns:
--  "id", "name", "type", "location", "founded_year"
INSERT INTO "schools"("name", "type", "location", "founded_year")
VALUES ('Harvard', 'University', 'Cambridge, Massachusetts', '1636');

-- The "companies" table contains the following columns:
--  "id", "name", "industry", "location"
INSERT INTO "companies" ("name", "industry", "location")
VALUES ('LinkdIn', 'Tecnology', 'Sunnyvale, California');

-- The "school_connections" table contains the following columns:
--  "id", "user_id", "school_id", "enrollment_date", "graduation_date", 
--  "degree_type",
INSERT INTO "school_connections" ("enrollment_date", "graduation_date", "degree_type", "user_id", "school_id")
VALUES
    ('1973-09-01', '1976-06-01', 'BA',
    (   SELECT "id"FROM "users"
        WHERE "first_name" = 'Alan' AND "last_name" = 'Garber'
    ), ( SELECT "id" FROM "schools" 
    WHERE "name" = 'Havard'));

-- The "company_connections" table contains the following columns:
--  "id", "user_id", "company_id", "start_date", "end_date", "position"
INSERT INTO "company_connections" ("start_date", "end_date", "position", "user_id", "company_id")
VALUES 
    ('2003-01-01', '2007-02-01', 'CEO', (
        SELECT "id" FROM "users"
        WHERE "first_name" = 'Reid' AND "last_name" = 'Hoffman'
    ),
    (
        SELECT "id" FROM "companies"
        WHERE "name" = 'LinkedIn'
    ));

