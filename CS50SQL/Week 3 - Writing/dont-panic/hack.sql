-- Set admin's password to the same password as user emily33
UPDATE "users"
SET "password" = (
    SELECT "password"
    FROM "users"
    WHERE "username" = 'emily33'
)
WHERE "username" = 'admin';
