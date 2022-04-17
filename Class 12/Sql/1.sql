-- Shows all the databases in the server
SHOW DATABASES;

-- Creates a new database
CREATE DATABASE photo_store;

-- Drop/Delete a  database
DROP DATABASE photo_store;

-- Changes the database to the one specified
use photo_store;

-- Shows the selected database
SELECT DATABASE();

-- Creates a table in the database
CREATE TABLE cameras(
    model_name VARCHAR(30),
    quantity INT
);

-- Shows the structure of the table
DESC cameras;

-- Drop/Delete table
DROP TABLE cameras;

-- Shows all the tables in the database
SHOW TABLES;

-- Inserts data into the table
INSERT INTO cameras(model_name, quantity)
VALUES("Nikon D7100", 10),
("Nikon 80D", 20),
("Nikon 15D", 25),
("Nikon E0S-R", 10);

-- Shows all the data in the table
SELECT * from canon_cameras;

-- Shows only model_name from the table
SELECT model_name from canon_cameras;

-- Shows model_name and quantity of a particular camera
SELECT model_name, quantity from canon_cameras
WHERE model_name='80d';

-- Shows model_name and quantity of a particular quantity
SELECT model_name, quantity from canon_cameras
WHERE quantity>=50;
