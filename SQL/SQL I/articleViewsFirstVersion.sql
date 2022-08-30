# Write your MySQL query statement below
#Table: Views (article_id,author_id,viewer_id,view_date) --> not PK
# same author_id and viewer_id --> same person
#Desirable output: author that read his article


SELECT DISTINCT author_id AS id FROM Views 
where author_id = viewer_id 
ORDER BY id ASC;
