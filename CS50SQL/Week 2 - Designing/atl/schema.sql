CREATE TABLE "passengers" (
    "id" INTEGER PRIMARY KEY,
    "first_name" TEXT,
    "last_name" TEXT,
    "age" INTEGER
);

CREATE TABLE "airlines" (
    "id" INTEGER PRIMARY KEY,
    "name" TEXT NOT NULL,
    "concourse" TEXT NOT NULL
);
