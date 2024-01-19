-- find earthquakes commonly categorized as "intermediate"
SELECT *
FROM earthquakes
WHERE depth>50 and depth <300
ORDER BY depth ASC
LIMIT 100;

-- find earthquakes that are incredibly damaging
SELECT *
FROM earthquakes
WHERE magnitude>7 and depth <300
ORDER by depth DESC;