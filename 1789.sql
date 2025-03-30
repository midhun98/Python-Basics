-- Simple but O(N²) time complexity

SELECT employee_id, department_id 
FROM Employee
WHERE primary_flag = 'Y'
OR employee_id IN (
    SELECT employee_id 
    FROM Employee
    GROUP BY employee_id
    HAVING COUNT(department_id) = 1
) 

-- O(N log N) time complexity 

SELECT e.employee_id, e.department_id 
FROM Employee e
LEFT JOIN (
    SELECT employee_id
    FROM Employee
    GROUP BY employee_id
    HAVING COUNT(department_id) = 1  
) single_dept
ON e.employee_id = single_dept.employee_id
WHERE e.primary_flag = 'Y'  
   OR single_dept.employee_id IS NOT NULL;
