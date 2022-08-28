# Write your MySQL query statement below
#GROUP_CONCAT --> concat names in one cell (same cell)
#show product solds by specific date!!

select sell_date, count( DISTINCT product ) as num_sold , GROUP_CONCAT( DISTINCT product order by product ASC) as products
    FROM Activities 
    GROUP BY sell_date 
    order by sell_date ASC;
