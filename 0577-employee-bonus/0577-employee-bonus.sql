# Write your MySQL query statement below
SELECT name, SUM(Bonus.bonus) as bonus FROM Employee
LEFT JOIN Bonus ON Employee.empId = Bonus.empId
WHERE bonus is NULL or bonus < 1000
GROUP BY Employee.empId
