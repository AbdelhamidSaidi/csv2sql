CREATE DATABASE etl_demo;
GO
USE etl_demo;

--creating tables

CREATE TABLE customers (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    country VARCHAR(50)
);

CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    customer_id INT,
    product VARCHAR(100),
    amount FLOAT,
    sale_date DATE
);

SELECT SYSTEM_USER;