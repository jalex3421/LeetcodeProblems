# Write your MySQL query statement below
# Users(id[int],name[varchar]) --> PK = id
# Rides(id[int],user_id[int],distance[int]) --> PK = id  //travels made by the user
# Output: travelled distance in desc order, name ascending order

SELECT name, SUM(IFNULL(distance,0)) AS travelled_distance
FROM Users LEFT JOIN Rides ON Users.id = Rides.user_id
GROUP BY Users.id
ORDER BY SUM(distance) DESC, name ASC
