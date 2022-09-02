# Write your MySQL query statement below
# Table (Orders: order_numeber[int], customer_number[int]) --> order_number=PK 
#       customer_number --> retrieve largest number of orders

select customer_number 
from orders
group by customer_number
order by count(*) desc limit 1;

