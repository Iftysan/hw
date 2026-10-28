import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

# SQL code to create the table, insert data, and query
sql_code = """
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary INTEGER NOT NULL
);

INSERT INTO employees VALUES (1, 'John', 'IT', 50000);
INSERT INTO employees VALUES (2, 'Mary', 'HR', 45000);
INSERT INTO employees VALUES (3, 'David', 'IT', 55000);
INSERT INTO employees VALUES (4, 'Sarah', 'Finance', 60000);
INSERT INTO employees VALUES (5, 'Peter', 'HR', 40000);

-- Select all employees
SELECT * FROM employees;

-- Select employees in the IT department
SELECT * FROM employees
WHERE department = 'IT';
"""

# Execute the SQL script
cursor.executescript(sql_code)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and queries executed successfully!")
