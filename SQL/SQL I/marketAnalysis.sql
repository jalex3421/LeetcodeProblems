# Write your MySQL query statement below
# Users(user_id[int],join_date[date],favorite_brand[varchar]) -->PK = user_id 
#       info of online shoppers: buy and sell items.
# Orders(order_id[int],order_date[date],item_id[int],buyer_id[int],seller_id[int])--> PK=order_id
#      FK = item_id --> ITEMS
#      FK = buyer_id and seller_id --> USERS
# Items(item_id[int],item_brand[varchar]) --> PK= item_id


# Using AND will put null in columns which doesn't match the condition...
# Where will filter the rows directly!!
SELECT u.user_id AS buyer_id, join_date, COUNT(order_date) AS orders_in_2019 
FROM Users as u LEFT JOIN Orders as o ON u.user_id = o.buyer_id
AND YEAR(order_date) = '2019'
GROUP BY u.user_id

