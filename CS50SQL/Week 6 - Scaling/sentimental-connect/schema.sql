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

CREATE TABLE `user_connections` (
    `id` INT UNSIGNED AUTO_INCREMENT,
    `user1_id` INT UNSIGNED,
    `user2_id` INT UNSIGNED,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`user1_id`) REFERENCES `users`(`id`),
    FOREIGN KEY(`user2_id`) REFERENCES `users`(`id`),

    CONSTRAINT unique_user_connection
    UNIQUE (`user1_id`, `user2_id`)
);

CREATE TABLE `school_connections` (
    `id` INT UNSIGNED AUTO_INCREMENT,
    `user_id` INT UNSIGNED,
    `school_id` INT UNSIGNED,
    `start` DATE,
    `end` DATE,
    `degree_type` VARCHAR(60),
    PRIMARY KEY(`id`),
    FOREIGN KEY(`user_id`) REFERENCES `users`(`id`),
    FOREIGN KEY(`school_id`) REFERENCES `schools`(`id`),

    CONSTRAINT unique_school_connections
    UNIQUE (`user_id`, `school_id`)
);


