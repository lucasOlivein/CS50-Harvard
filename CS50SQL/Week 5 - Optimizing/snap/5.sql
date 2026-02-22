-- Task: Given two usernames, lovelytrust487 and 
-- exceptionalinspiration482, find the user IDs of their 
-- mutual friends.

-- A mutual friend is a user that both lovelytrust487 and 
-- exceptionalinspiration482 count among their friends.


-- user table               -- friend table

-- id                       - user_id
-- username                 - friend_id
-- phone_number             - friendship_date
-- joined_date
-- joined_date

SELECT "friend_id"
FROM "friends"
WHERE "user_id" = (
    SELECT "id"
    FROM "users"
    WHERE "username" = 'lovelytrust487'
)
INTERSECT
SELECT "friend_id"
FROM "friends"
WHERE "user_id" = (
    SELECT "id"
    FROM "users"
    WHERE "username" = 'exceptionalinspiration482' 
);