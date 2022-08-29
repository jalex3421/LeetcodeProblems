# Write your MySQL query statement below

SELECT employee_id
FROM Salaries
WHERE Salaries.employee_id not in
(
    SELECT employee_id
    FROM Employees
)
UNION
SELECT employee_id
FROM Employees
WHERE Employees.employee_id not in
(
    SELECT employee_id
    FROM Salaries
)
order by employee_id asc;
