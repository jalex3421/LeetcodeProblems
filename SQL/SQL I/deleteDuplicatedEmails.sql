# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below


#delete duplicated emails associated with the largest id --> table_name: Person
#columns: id and email


#use alias in order to use twice the same table
DELETE p1 FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id;
