-- find earthquakes commonly categorized as "intermediate"
SELECT *
FROM earthquakes
WHERE depth>50 and depth <300
ORDER BY depth ASC
LIMIT 50;

-- find earthquakes that are incredibly damaging
SELECT *
FROM earthquakes
WHERE magnitude>6 and depth <300
ORDER by depth DESC;

-- find earthquakes in Texas by text matching
SELECT *
FROM earthquakes
WHERE 'tx' ~ locationSource
ORDER BY magnitude DESC;

SELECT * FROM earthquakes WHERE longitude BETWEEN -180 AND -130 AND latitude BETWEEN 52 AND 71;

