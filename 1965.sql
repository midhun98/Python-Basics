-- MySQL
SELECT employee_id
FROM Employees
LEFT JOIN Salaries USING (employee_id)
WHERE salary IS NULL

UNION

SELECT employee_id
FROM Salaries
LEFT JOIN Employees USING (employee_id)
WHERE name IS NULL

ORDER BY employee_id;


-- PostgresSQL


SELECT employee_id 
FROM Employees 
FULL OUTER JOIN Salaries 
USING (employee_id) 
WHERE name IS NULL OR salary IS NULL 
order by employee_id;