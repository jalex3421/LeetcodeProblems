# Write your MySQL query statement below
# Table: Logins(user_id[int], time_stamp[date]) --> PK = (user_id, time_stamp)
# Desirable output: latest login for all users in 2020

#The use of max function will output the last stamp
SELECT user_id, MAX(time_stamp) AS last_stamp 
FROM Logins
WHERE YEAR(time_stamp) = 2020 #filtering for login dates with year 2020 in timestamp
GROUP BY user_id;

