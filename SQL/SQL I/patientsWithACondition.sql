# Write your MySQL query statement below
#show patiens with diabetes type I --> start with DIAB1 prefix (also contains diabetes in condition)

SELECT patient_id, patient_name, conditions
FROM PATIENTS 
WHERE CONDITIONS LIKE '% DIAB1%' OR CONDITIONS LIKE 'DIAB1%';
