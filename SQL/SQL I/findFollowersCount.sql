# Write your MySQL query statement below
# Table: Followers(user_id[int],follower_id[int]) --> PK the pair
#Return number of followers associated to an id

select user_id, count(distinct follower_id) as followers_count
from Followers
group by user_id;
