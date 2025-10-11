WITH cte AS (
    SELECT player_id,
        MIN(event_date) as first_day
    FROM Activity
    GROUP BY player_id
),
cte2 AS(
    SELECT *,
        DATE_ADD(first_day, INTERVAL 1 DAY) AS next_day
    FROM cte
)
SELECT ROUND(
        (
            SELECT COUNT(*)
            FROM Activity
            WHERE (player_id, event_date) IN (
                    SELECT player_id,
                        next_day
                    FROM cte2
                )
        ) / (
            SELECT COUNT(DISTINCT player_id)
            FROM Activity
        ),
        2
    ) AS fraction

