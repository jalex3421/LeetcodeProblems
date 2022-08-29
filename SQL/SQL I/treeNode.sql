# Write your MySQL query statement below

#'type' is the name of a column...

SELECT id,
    CASE 
        WHEN p_id IS NULL THEN 'Root'
        WHEN id IN (SELECT p_id FROM Tree)THEN 'Inner'
        ELSE 'Leaf'
        END AS type
 FROM Tree
