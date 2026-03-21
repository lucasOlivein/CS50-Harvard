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

CREATE TABLE `schools` (
    `id` INT UNSIGNED AUTO_INCREMENT,
    `school_name` VARCHAR(60),
    `school_type` ENUM('Primary', 'Secondary', 'Higher Education'),
    `location` VARCHAR(60),
    `year` SMALLINT UNSIGNED,
    PRIMARY KEY(`id`),

    CONSTRAINT unique_school
    UNIQUE (`school_name`, `school_type`, `location`)
);

CREATE TABLE `companies` (
    `id` INT UNSIGNED AUTO_INCREMENT,
    `name` VARCHAR(60),
    `industry` ENUM('Technology', 'Education', 'Business'),
    `location` VARCHAR(60),
    PRIMARY KEY(`id`),

    CONSTRAINT unique_company
    UNIQUE (`name`, `industry`, `location`)
);


