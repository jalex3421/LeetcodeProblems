# Write your MySQL query statement below
#In this situation we want to swap salaries between mens and womes

UPDATE salary
SET
    sex = CASE sex
        WHEN 'm' THEN 'f'
        ELSE 'm'
    END;
