-- The "users" table contains the following columns:
--  "id", "first_name", "last_name", "username", "password"
INSERT INTO `users` (`first_name`, `last_name`, `username`, `password`)
VALUES (
    ('Claudine', 'Gay', 'claudine', 'password'),
    ('Reid', 'Hoffman', 'reid', 'password')
);

-- The "schools" table contains the following columns:
--  "id", "school_name", "school_type", "location", "year"
INSERT INTO `schools` (`school_name`, `school_type`, `location`, `year`)
VALUES ('Harvard University', 'Higher Education','Cambridge, Massachusetts', 1636);

-- The "companies" table contains the following columns:
--  "id", "name", "industry", "location"
INSERT INTO `companies` (`name`, `industry`, `location`)
VALUES ('LinkedIn', 'Technology', 'Sunnyvale, California');

-- The "school_connections" table contains the following columns:
--  "id", "user_id", "school_id", "start", "end",
--  "degree_type",
INSERT INTO `school_connections`(`user_id`, `school_id`, `start`, `end`, `degree_type`)
VALUES ( 
        (SELECT `id`FROM `users`WHERE `first_name` = 'Claudine' AND `last_name` = 'Gay'),
        (SELECT `id` FROM `schools`WHERE `school_name` = 'Harvard University'),
        '1993-01-01', '1998-12-31', 'PhD'
        );

-- The "company_connections" table contains the following columns:
--  "id", "user_id", "company_id", "start", "end", "title"
INSERT INTO `company_connections`(`user_id`, `company_id`, `start`, `end`, `title`)
VALUES(
    (SELECT `id` FROM `users` WHERE `first_name` = 'Reid' AND `last_name` = 'Hoffman'),
    (SELECT `id` FROM `companies` WHERE `name` = 'LinkedIn'),
    '2003-01-01', '2007-02-01', 'CEO and Chairman'
);
