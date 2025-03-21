CREATE TABLE employees (
    employee_id INT PRIMARY KEY NOT NULL,
    name VARCHAR(11) NOT NULL,
    manager_id INT
);

INSERT INTO employees (employee_id, name, manager_id) VALUES
(1, 'Head Honcho', NULL),
(2, 'Bob', 1),
(3, 'Alice', 1),
(4, 'John', 1),
(5, 'Frank', 2),
(6, 'Steve', 4),
(7, 'Mary', 2),
(8, 'Joe', 3),
(9, 'Chunk', 6),
(10, 'Larry', 8),
(11, 'Phil', 9),
(12, 'David', 4),
(13, 'Henry', 5),
(14, 'Eve', 12),
(15, 'Gracie', 13);
