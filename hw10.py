import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Execute the SQL code
sql_code = """
CREATE TABLE IF NOT EXISTS Employee (
  employee_id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  city TEXT NOT NULL,
  commission REAL
);

INSERT INTO Employee (employee_id, name, city, commission)
VALUES
  ("5001", "James Hoog", "New York", 150.0),
  ("5002", "Nail Knite", "Paris", 130.0),
  ("5005", "Pit Alex", "London", 110.0),
  ("5006", "Mc Lyon", "Paris", 140.0),
  ("5007", "Paul Adam", "Rome", 130.0),
  ("5003", "Lauson Hen", "San Jose", 120.0);

CREATE TABLE IF NOT EXISTS Customer (
  customer_id TEXT PRIMARY KEY,
  cust_name TEXT NOT NULL,
  city TEXT NOT NULL,
  grade INTEGER,
  employee_id TEXT,
  FOREIGN KEY (employee_id) REFERENCES Employee (employee_id)
);

INSERT INTO Customer (customer_id, cust_name, city, grade, employee_id)
VALUES
  ("3002", "Nick Rimando", "New York", 100, "5001"),
  ("3007", "Brad Davis", "New York", 200, "5001"),
  ("3005", "Graham Zusi", "California", 200, "5002"),
  ("3008", "Julian Green", "London", 300, "5002"),
  ("3004", "Fabian Johnson", "Paris", 300, "5006");
"""

# Execute the SQL script
cursor.executescript(sql_code)

# Commit changes and close the connection
conn.commit()
conn.close()