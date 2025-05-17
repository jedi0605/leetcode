# Write your MySQL query statement below
SELECT Product.product_name, sales.year, sales.price
FROM sales
LEFT JOIN Product ON sales.product_id = Product.product_id