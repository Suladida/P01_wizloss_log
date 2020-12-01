-- Database table info goes here
DROP TABLE IF EXISTS losses;
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS wizards;

CREATE TABLE wizards (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    type VARCHAR(255),
    colour VARCHAR(255),
    style VARCHAR(255),
    wizard_id INT REFERENCES wizards(id) ON DELETE CASCADE
);

CREATE TABLE losses (
    id SERIAL PRIMARY KEY,
    day INT,
    month INT,
    year INT,
    details VARCHAR(255),
    wizard_id INT REFERENCES wizards(id) ON DELETE CASCADE,
    item_id INT REFERENCES items(id) ON DELETE CASCADE,
    recovered BOOLEAN 
);