CREATE TABLE "ingredients" (
    "id" INTEGER PRIMARY KEY,
    "name" TEXT NOT NULL,
    "price" REAL NOT NULL,
    "unit" TEXT NOT NULL
);

CREATE TABLE "donuts" (
    "id" INTEGER PRIMARY KEY,
    "name" TEXT,
    "gluten-free" TEXT NOT NULL,
    "price" REAL
);

CREATE TABLE "customers" (
    "id" INTEGER PRIMARY KEY,
    "first_name" TEXT,
    "last_name" TEXT
);

CREATE TABLE "orders" (
    "id" INTEGER PRIMARY KEY,
    "order_number" INTEGER NOT NULL,
    "customer_id" INTEGER,
    FOREIGN KEY("customer_id") REFERENCES "customers"("id")
);
