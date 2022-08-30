# Write your MySQL query statement below


#Tables=> Person (personId) and Address (personId) 

#The LEFT JOIN keyword returns all records from the left table (table1), and the matching records from the right table (table2). The result is 0 records from the right side, if there is no match.

select firstName, lastName, city, state
from Person left join Address
on Person.personId = Address.personId;
