-- 1) Create three tables (if they don’t already exist):
--    a) Salesman table: store salesman id, name, city, commission.
--    b) Customer table: store customer id, customer name, city, grade, and salesman id.
--    c) Orders table: store order number, purchase amount, date, customer id, and salesman id.

-- 2) Insert sample data into each table:
--    a) Use `INSERT INTO ... VALUES` with multiple rows for Salesman.
--    b) Do the same for Customer.
--    c) Do the same for Orders.

-- 3) Write JOIN queries to fetch combined data:
--    a) Match customers and salesmen who are from the same city.
--    b) Link each customer to their salesman using salesman id.
--    c) Show orders where customer city and salesman city are different.
--    d) Show all orders along with customer names.

-- 4) Filtered reports:
--    a) Show customers (with their grade) where grade is present (not NULL).
--    b) Show customers + salesmen where commission lies between 0.12 and 0.14.
--    c) Calculate commission amount for orders where customer grade is 200 or more:
--       - Commission Amount = purchase amount * commission rate.

-- 5) Date-based query:
--    a) Show customer and order details for orders placed on a specific date.