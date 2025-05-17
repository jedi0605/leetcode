# Write your MySQL query statement below
SELECT W1.id
FROM Weather as W1
LEFT JOIN Weather as W2 on DATEDIFF(W1.recordDate, W2.recordDate) = 1
WHERE W1.temperature > W2.temperature
