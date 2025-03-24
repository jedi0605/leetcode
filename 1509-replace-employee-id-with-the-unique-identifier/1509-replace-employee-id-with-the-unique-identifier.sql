# Write your MySQL query statement below
Select Employees.name,EmployeeUNI.unique_id  From Employees
left JOIN EmployeeUNI
ON Employees.id = EmployeeUNI.id;