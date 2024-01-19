-- find earthquakes commonly categorized as "intermediate"
SELECT *
FROM earthquakes
WHERE depth>50 and depth <300
ORDER BY depth DESC;