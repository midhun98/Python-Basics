SELECT
  query_name,
  Round(Avg(rating / position), 2) AS quality,
  Round(Avg(IF (rating < 3, 1, 0)) * 100, 2) AS poor_query_percentage
FROM
  queries
GROUP BY
  query_name