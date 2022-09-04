# Write your MySQL query statement below
# Person(id[int],emil[varchar]) --> PK = id
#show all the duplicated emails

select email
from Person
group by email
having count(*)>1;

