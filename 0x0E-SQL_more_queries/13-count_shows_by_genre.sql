-- A script that lists genres and the number of shows linked to each 
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked
-- can use only one SELECT statement

SELECT g.name AS genre,
       COUNT(*) AS number_of_shows
  FROM tv_genres AS g
       INNER JOIN tv_show_genres AS t
       ON g.id = t.genre_id
 GROUP BY g.name
 ORDER BY number_of_shows DESC;
