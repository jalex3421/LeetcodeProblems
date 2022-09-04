# Write your MySQL query statement below
# ActorDirector(actor_id[int],director_id[int].timestamp[int]) --> PK=timestamp
# Output: actor cooperated with director at least three times

SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id,director_id
HAVING COUNT(*)>2;
