-- Task: Find the user IDs of the top 3 users to whom creativewisdom377 
-- sends messages most frequently.
-- Order the user IDs by the number of messages creativewisdom377 has 
-- sent to those users, most to least.

-- messages table           users table

-- id                       - id
-- from_user_id             - username
-- to_user_id               - phone_number
-- picture                  - joined_date
-- sent_timestamp           - last_login_date
-- viewed_timestamp
-- expires_timestamp

SELECT "to_user_id"
FROM "messages"
WHERE "from_user_id" = (
    SELECT "id" FROM "users"
    WHERE "username" = 'creativewisdom377')
GROUP BY "to_user_id"
ORDER BY COUNT("to_user_id") DESC
LIMIT 3;