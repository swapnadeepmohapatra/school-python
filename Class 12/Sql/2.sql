-- Create new table with primary key and default value
CREATE TABLE customers(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(30) NOT NULL,
	email VARCHAR(40) NOT NULL DEFAULT 'no email provided',
	amount INT,
	PRIMARY KEY(id)
);

-- Insert data into table
INSERT INTO customers(name, email, amount)
VALUES('John', "john@doe.com", 100);

-- Shows only names from the table
SELECT name from customers;

-- Shows only emails from the table
SELECT email from customers;

-- Shows data with custom header (alias)
SELECT amount AS Purchases from customers;

-- Update email, according to the name
UPDATE customers SET email="john@gmail.com" WHERE name = "John";

-- Update amount, according to the id
UPDATE customers SET amount=500 WHERE id = 6; 

-- Delete data, according to the id
DELETE FROM customers WHERE id = 9;