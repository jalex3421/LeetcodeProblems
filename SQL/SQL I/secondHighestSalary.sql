# Write your MySQL query statement below

#SHOW SECOND HIGHEST SALARY

SELECT max(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT max(Salary) FROM Employee)
