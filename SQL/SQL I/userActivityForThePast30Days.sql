# Write your MySQL query statement below
# Table: Activity(user_id,session_id,activity_date,activity_type)
#       It could be duplicated rows. There is no primary key.
#        activity_type --> ENUM 
# Output: activities for a period of 30 days ending 2019-07-27
#         User activity if they made at least one activity a day

#First approach: show the columns to display
#Second approach: filter based on the date
#Third approach: group by date
select activity_date AS day, count(distinct user_id) as active_users
from Activity
where (activity_date > "2019-06-27" AND activity_date <= "2019-07-27")
group by activity_date;
