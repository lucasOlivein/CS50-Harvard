-- Task: Find when the message with ID 151 expires. 
-- You may use the message’s ID directly in your query.

-- messages table

-- Columns
-- id
-- from_user_id
-- to_user_id
-- picture
-- sent_timestamp
-- viewed_timestamp
-- expires_timestamp


SELECT "expires_timestamp" FROM messages
WHERE "id" = 151;
