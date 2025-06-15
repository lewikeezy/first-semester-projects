--Basic Queries--

-- All customers
SELECT * FROM customers;

-- All products
SELECT * FROM products;

-- Filter products by category (e.g., Drinks)
SELECT * FROM products WHERE category = 'Drinks';

-- Recent orders by date
SELECT * FROM orders ORDER BY order_date DESC;


--Aggregators Queries--
-- Total number of orders
SELECT COUNT(*) AS total_orders FROM orders;

-- Revenue per product (price × quantity)
SELECT 
    p.product_name, 
    SUM(p.price * o.quantity) AS total_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name;

-- Average product price
SELECT AVG(price) AS average_price FROM products;


-- Joins Queries --

-- Detailed order information (INNER JOIN)
SELECT 
    o.order_id, 
    c.name AS customer_name, 
    p.product_name, 
    o.quantity, 
    o.order_date
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN products p ON o.product_id = p.product_id;

-- List all customers and their orders (LEFT JOIN)
SELECT 
    c.name AS customer_name, 
    o.order_id, 
    o.order_date
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;

-- List all products even if not ordered (LEFT JOIN)
SELECT 
    p.product_name, 
    o.order_id
FROM products p
LEFT JOIN orders o ON p.product_id = o.product_id;
