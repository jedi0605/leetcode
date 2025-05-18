# Write your MySQL query statement below
SELECT A1.machine_id,ROUND( SUM((A2.timestamp - A1.timestamp))/COUNT(*),3) as processing_time
FROM Activity as A1
LEFT JOIN Activity as A2
ON A1.machine_id = A2.machine_id AND A1.process_id = A2.process_id
Where A1.activity_type = 'start' and A2.activity_type = 'end'
GROUP BY A1.machine_id