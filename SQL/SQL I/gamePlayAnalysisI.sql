# Write your MySQL query statement below
# Table: Activity(player_id[int],device_id[int],event_date[date],games_played[int]) --> PK=(player_id,event_date)
# Desirable output: return the first loggin associated to a user

select player_id, min(event_date) as first_login
from activity 
group by player_id;

