-- Fetch all employees
SELECT * FROM employees;

-- Count total employees
SELECT COUNT(*) AS total_employees
FROM employees;

-- Average salary by department
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;

-- Highest paid employee
SELECT *
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

-- Employees joined in 2023
SELECT *
FROM employees
WHERE YEAR(join_date) = 2023;

-- Employee count per department
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department;
