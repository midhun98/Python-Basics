WITH cte AS(
    SELECT requester_id AS id,
        accepter_id AS friend_id
    FROM RequestAccepted
    UNION
    SELECT accepter_id AS id,
        requester_id as friend_id
    FROM RequestAccepted
)
SELECT id,
    COUNT(DISTINCT friend_id) AS num
FROM cte
GROUP BY id
ORDER BY num DESC
LIMIT 1