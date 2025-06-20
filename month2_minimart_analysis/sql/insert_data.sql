-- SQL script to insert sample data

-- Insert sample customers
INSERT INTO customers (name, email, join_date) VALUES
('Michael Johnson', 'johnson@alt.com', '2024-01-15'),
('Usian Bolt', 'bolt@alt.com', '2024-02-10'),
('Asafa Powell', 'Powell@alt.com', '2024-03-01'),
('Anthony Joshua', 'joshua@alt.com', '2024-03-18'),
('Christiano Ronaldo', 'Ronaldo@alt.com', '2024-04-05');

-- Insert sample products
INSERT INTO products (product_name, category, price) VALUES
('Coca-Cola', 'Drinks', 1.50),
('Bread', 'Bakery', 2.00),
('Toothpaste', 'Toiletries', 3.00),
('Orange Juice', 'Drinks', 2.50),
('Chips', 'Snacks', 1.80);

-- Insert sample orders (customer and product IDs match order of insert)
INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES
(1, 1, 2, '2024-04-10'),
(2, 3, 1, '2024-04-11'),
(3, 2, 3, '2024-04-12'),
(1, 5, 4, '2024-04-13'),
(4, 4, 1, '2024-04-14');

