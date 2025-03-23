SELECT DISTINCT w1.id as Id
FROM weather w1
JOIN weather w2
ON w1.recordDate - INTERVAL 1 DAY = w2.recordDate
WHERE w1.temperature  > w2.temperature