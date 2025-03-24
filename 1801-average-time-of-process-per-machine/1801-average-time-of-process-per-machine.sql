# Write your MySQL query statement below
SELECT A1.machine_id, ROUND( SUM(A1.timestamp - A2.timestamp) / COUNT(A1.machine_id),3) as processing_time FROM Activity as A1
JOIN Activity as A2 on A1.machine_id = A2.machine_id and A1.process_id = A2.process_id and A2.activity_type = "start"
WHERE A1.activity_type='end'
GROUP BY A1.machine_id