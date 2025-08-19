import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

# employees = pd.read_sql("""
#     SELECT * FROM employees;
# """, conn)

# print(employees)


pattersons = pd.read_sql("""
    SELECT * FROM employees
    WHERE lastName = "Patterson";
""", conn)

print(pattersons)


employees_first_fiveLetters = pd.read_sql("""
    SELECT *, length(firstName) AS name_length FROM employees
    WHERE name_length = 5;
""", conn)

print(employees_first_fiveLetters)



employees_initial_l = pd.read_sql("""
    SELECT *, substr(firstName, 1, 1) AS first_initial FROM employees
    WHERE first_initial = "L";
""", conn)

print(employees_initial_l)


price_each_thirty = pd.read_sql("""
    SELECT *, CAST(round(priceEach) AS INTEGER) AS rounded_price_int FROM orderDetails
    WHERE rounded_price_int = 30;
""", conn)

print(price_each_thirty)



january_orders = pd.read_sql("""
    SELECT *, strftime("%m", orderDate) AS month FROM orders
    WHERE month = "01";
""", conn)

print(january_orders)



late_shipped_orders = pd.read_sql("""
    SELECT *, julianday(shippedDate) - julianday(requiredDate) AS days_late FROM orders
    WHERE days_late > 0;
""", conn)

print(late_shipped_orders)


conn.close()