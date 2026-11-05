-- Generate 100 users.
INSERT INTO users (name, email)
SELECT
    'User ' || generate_series,
    'user' || generate_series || '@example.com'
FROM generate_series(1, 100);

-- Generate 2 orders for every user.
INSERT INTO orders (user_id, amount)
SELECT
    user_id,
    1000 + (order_number * 500)
FROM generate_series(1, 100) AS user_id
CROSS JOIN generate_series(1, 2) AS order_number;