SELECT (
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC OFFSET 1
        LIMIT 1
    ) AS SecondHighestSalary;
-- 
-- using dense rank
SELECT MAX(salary) AS SecondHighestSalary
FROM (
        SELECT salary,
            DENSE_RANK() OVER (
                ORDER BY salary DESC
            ) AS rnk
        FROM Employee
    ) t
WHERE rnk = 2;