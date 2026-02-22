-- Task: Find the username of the most popular user, defined
-- as the user who has had the most messages sent to them.

-- messages table           users table

-- id                       - id
-- from_user_id             - username
-- to_user_id               - phone_number
-- picture                  - joined_date
-- sent_timestamp           - last_login_date
-- viewed_timestamp
-- expires_timestamp


SELECT "username"
FROM "users"
WHERE "users"."id" = (
    SELECT "to_user_id"
    FROM "messages"
    GROUP BY "to_user_id"
    ORDER BY COUNT("to_user_id") DESC
    LIMIT 1
);