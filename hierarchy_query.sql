WITH RECURSIVE hierarchy AS (
    -- base case
    SELECT 
        employee_id,
        name,
        CAST(NULL AS VARCHAR) AS manager_hierarchy,
        1 AS level
    FROM employees
    WHERE manager_id IS NULL
    
    -- add all rows together without checking for duplicates
    UNION ALL
    
    -- build row for row
    SELECT 
        employee.employee_id,
        employee.name,
        CASE 
            WHEN manager.manager_hierarchy IS NULL THEN manager.name
            ELSE CONCAT(manager.manager_hierarchy, ' -> ', manager.name)
        END AS manager_hierarchy,
        manager.level + 1 AS level
    FROM employees AS employee
    JOIN hierarchy AS manager ON employee.manager_id = manager.employee_id
)

SELECT 
    employee_id, 
    name, 
    manager_hierarchy,
    level
FROM hierarchy
ORDER BY level, employee_id;
