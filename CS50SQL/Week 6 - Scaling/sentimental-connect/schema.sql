CREATE TABLE `users` (
    `id` INT UNSIGNED AUTO_INCREMENT,
    `first_name` VARCHAR(60),
    `last_name` VARCHAR(60),
    `username` VARCHAR(60),
    `password` VARCHAR(128),
    PRIMARY KEY(`id`),

    CONSTRAINT unique_username
    UNIQUE (`username`)
);

