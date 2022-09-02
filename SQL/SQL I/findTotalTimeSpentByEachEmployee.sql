# Write your MySQL query statement below
# Table: Employees(emp_id[int],event_day[date],in_time[int],out_time[int])
# PK => emp_id,event_day,in_time
# event_day : day which event happened
# in_time: minute at which the employeed entered the office
# out_time: minute the empployeed left the office
# in_time < out_time
#Desirable output: Minutes spent by each employee on each day at the office

SELECT event_day AS day, emp_id, SUM(out_time - in_time) AS total_time
FROM Employees
GROUP BY event_day, emp_id;
