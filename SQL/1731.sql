SELECT e1.employee_id, e1.name, 
COUNT(e2.employee_id) AS reports_count, 
ROUND(AVG(e2.age)) AS average_age 
FROM Employees e1 -- imagine as manager table
JOIN Employees e2 -- imagine as employee table
ON e1.employee_id = e2.reports_to
GROUP BY e1.employee_id, e1.name
ORDER BY e1.employee_id