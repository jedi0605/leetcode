# Write your MySQL query statement below
SELECT author_id as id
FROM views
WHERE author_id = viewer_id

GROUP BY id
Order by id asc
