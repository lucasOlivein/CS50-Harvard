CREATE TABLE "users" (
    "id" INTEGER PRIMARY KEY,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "username" TEXT NOT NULL,
    "password" TEXT NOT NULL
);

CREATE TABLE "schools" (
    "id" INTEGER PRIMARY KEY,
    "name" TEXT NOT NULL,
    "type" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    "founded_year" INTEGER
);

CREATE TABLE "companies" (
    "id" INTEGER PRIMARY KEY,
    "name" TEXT NOT NULL,
    "industry" TEXT NOT NULL,
    "location" TEXT NOT NULL
);

CREATE TABLE "users_connections" (
    "id" INTEGER PRIMARY KEY,
    "user1_id" INTEGER,
    "user2_id" INTEGER 
);

CREATE TABLE "school_connections" (
    "id" INTEGER PRIMARY KEY,
    "user_id" INTEGER,
    "school_id" INTEGER,
    "enrollment_date" TEXT NOT NULL,
    "graduation_date" TEXT NOT NULL,
    "degree_type" TEXT NOT NULL,
    FOREIGN KEY("user_id") REFERENCES "users"("id"),
    FOREIGN KEY("school_id") REFERENCES "schools"("id")
);

CREATE TABLE "company_connections" (
    "id" INTEGER PRIMARY KEY,
    "user_id" INTEGER,
    "company_id" INTEGER,
    "start_date" TEXT NOT NULL,
    "end_date" TEXT NOT NULL,
    "position" TEXT NOT NULL,
    FOREIGN KEY("user_id") REFERENCES "users"("id"),
    FOREIGN KEY("company_id") REFERENCES "company"("id")
);
