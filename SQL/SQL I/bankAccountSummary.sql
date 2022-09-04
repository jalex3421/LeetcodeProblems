# Write your MySQL query statement below
# Users(account[int],name[varchar]) --> PK=account
# Transactions(trans_id[int],account[int],amoun[int],transacted_on[date]) --> PK=trans_id

SELECT Users.name, sum(amount) as balance
FROM Transactions, Users
WHERE users.account = Transactions.account
GROUP BY users.account
HAVING balance > 10000
