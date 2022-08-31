# Write your MySQL query statement below

#Tables: SalesPerson(sales_id,name,salary,commision_rate,hire_date) --> PK=sales_id
#        Company(com_id,name,city) --> PK=com_id
#        Orders(order_id,order_date,com_id,sales_id,amount) --> PK=order_id, FK=com_id & sales_id

#Output: names of salesperson who did not have any order to the company "RED"


#LEFT JOIN: it could be a first approach. Then an idea based on 'not in' is also a good thing...

select SalesPerson.name as 'name'
from SalesPerson
where SalesPerson.sales_id not in 
(select o.sales_id
 from Orders o left join Company c 
              on o.com_id = c.com_id
where c.name = 'RED');
