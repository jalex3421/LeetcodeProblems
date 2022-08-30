# Write your MySQL query statement below

#Tables: Visits (visit_id, customer_id), Transactions (transaction_id, visit_id, amount)
#Output: users who have made a visit and the number of times they have made these types of visits whithout making any transaction

SELECT customer_id , COUNT(Visits.visit_id) AS count_no_trans
FROM Visits LEFT JOIN Transactions
	ON Visits.visit_id = Transactions.visit_id
WHERE 
	Transactions.transaction_id IS NULL
GROUP BY customer_id
