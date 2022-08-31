# Write your MySQL query statement below
# Table: Weather(id,recordDate,temperature)
# Desirable output: return id associated to days that have higher temps that previous day

#we can use Join() and Datediff()-->compare two data type values

SELECT weather.id AS 'Id'
FROM weather
        JOIN
    weather w ON DATEDIFF(weather.recordDate, w.recordDate) = 1
    AND weather.Temperature > w.Temperature ;
