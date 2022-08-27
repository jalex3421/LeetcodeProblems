# Write your MySQL query statement below
#bonus if the id of the employer is an odd number and the name start with 'M'

#Make bonus if employee_id is not odd, and the name start with 'm' letter...


SELECT employee_id,
IF (employee_id%2 AND name not like "M%", salary, 0) as bonus
FROM Employees 
order by employee_id;
