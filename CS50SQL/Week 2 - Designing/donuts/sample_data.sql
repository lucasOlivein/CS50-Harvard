-- The "ingredients" table contains the following columns:
--  "id", "name", "price", "unit"
INSERT INTO "ingredients" ("name", "price", "unit")
VALUES 
    ('Cocoa', 5.00, 'pound'),
    ('Sugar', 2.00, 'pound'),
    ('Flour', 1.50, 'pound'),
    ('Buttermilk', 3.00, 'liter'),
    ('Sprinkles', 8.00, 'pound');

-- The "donuts" table contains the following columns:
--  "id", "name", "gluten-free", "price"
INSERT INTO "donuts" ("name", "gluten-free", "price")
VALUES ('Belgian Dark Chocolate', 'No', 4.00),
    ('Back-To-School Sprinkles', 'No', 4.00);

-- The "ingredients per donut" table contains the following columns:
--  "id", "ingredient_id", "donut_id"
INSERT INTO "ingredients per donut" ("donut_id", "ingredient_id")
VALUES
--  Belgian Dark Chocolate's ingredients
    ((SELECT "id" FROM "donuts" WHERE "name" = 'Belgian Dark Chocolate'),
     (SELECT "id" FROM "ingredients" WHERE "name" = 'Cocoa')),
     ((SELECT "id" FROM "donuts" WHERE "name" = 'Belgian Dark Chocolate'),
     (SELECT "id" FROM "ingredients" WHERE "name" = 'Flour')),
     ((SELECT "id" FROM "donuts" WHERE "name" = 'Belgian Dark Chocolate'),
     (SELECT "id" FROM "ingredients" WHERE "name" = 'Buttermilk')),
     ((SELECT "id" FROM "donuts" WHERE "name" = 'Belgian Dark Chocolate'),
     (SELECT "id" FROM "ingredients" WHERE "name" = 'Sugar')),
-- Back-To-School Sprinkles's ingredients
    ((SELECT "id" FROM "donuts" WHERE "name" = 'Back-To-School Sprinkles'),
     (SELECT "id" FROM "ingredients" WHERE "name" = 'Flour')),
     ((SELECT "id" FROM "donuts" WHERE "name" = 'Back-To-School Sprinkles'),
     (SELECT "id" FROM "ingredients" WHERE "name" = 'Buttermilk')),
     ((SELECT "id" FROM "donuts" WHERE "name" = 'Back-To-School Sprinkles'),
     (SELECT "id" FROM "ingredients" WHERE "name" = 'Sugar')),
     ((SELECT "id" FROM "donuts" WHERE "name" = 'Back-To-School Sprinkles'),
     (SELECT "id" FROM "ingredients" WHERE "name" = 'Sprinkles'));

-- The "customers" table contains the following columns:
--  "id", "first_name", "last_name"
INSERT INTO "customers" ("first_name", "last_name")
VALUES ('Luis', 'Singh');

-- The "orders" table contains the following columns:
-- "id", "order_number", "customer_id"
INSERT INTO "orders" ("order_number", "customer_id")
VALUES (1, (SELECT "id" FROM "customers" WHERE "first_name" = 'Luis' AND "last_name" = 'Singh'));

-- The "donuts per order" table constains the following columns:
--  "id", "order_id", "donut_id"
INSERT INTO "donuts per order" ("order_id", "donut_id")
-- Order: 3 Belgian Dark Chocolate and 2 Back-To-School Sprinkles
-- Customer: Luis Singh
VALUES 
-- 3 Belgian Dark Chocolate
    ((SELECT "id" FROM "orders" WHERE "customer_id" = (SELECT "id" FROM "customers" WHERE "first_name" = 'Luiz' AND "last_name" = 'Singh')),
     (SELECT "id" FROM "donuts" WHERE "name" = 'Belgian Dark Chocolate')),
     ((SELECT "id" FROM "orders" WHERE "customer_id" = (SELECT "id" FROM "customers" WHERE "first_name" = 'Luiz' AND "last_name" = 'Singh')),
     (SELECT "id" FROM "donuts" WHERE "name" = 'Belgian Dark Chocolate')),
     ((SELECT "id" FROM "orders" WHERE "customer_id" = (SELECT "id" FROM "customers" WHERE "first_name" = 'Luiz' AND "last_name" = 'Singh')),
     (SELECT "id" FROM "donuts" WHERE "name" = 'Belgian Dark Chocolate')),
-- 2 Back-To-School Sprinkles
    ((SELECT "id" FROM "orders" WHERE "customer_id" = (SELECT "id" FROM "customers" WHERE "first_name" = 'Luiz' AND "last_name" = 'Singh')),
    (SELECT "id" FROM "donuts" WHERE "name" = 'Back-To-School Sprinkles')),
     ((SELECT "id" FROM "orders" WHERE "customer_id" = (SELECT "id" FROM "customers" WHERE "first_name" = 'Luiz' AND "last_name" = 'Singh')),
     (SELECT "id" FROM "donuts" WHERE "name" = 'Back-To-School Sprinkles'));