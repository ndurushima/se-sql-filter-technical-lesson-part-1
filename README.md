# Technical Lesson Part 1: Filtering Data with SQL

For this part of the lesson, we'll start by using the Northwind database, the ERD (Entity Relationship Diagram) of which is shown below. We will use this database to illustrate how SELECT and WHERE are used to filter data. In particular, filtering in SQL using SELECT and WHERE allows you to retrieve specific data from a database table. The SELECT statement specifies which columns you want to retrieve, while the WHERE clause defines conditions that rows must meet to be included in the results. Together, they let you extract precisely the data you need.
<br /><br />
For example, below we will use SELECT to select all orders placed in January of any year. To demonstrate WHERE, we’ll use a cats database. We’ll see, for instance, how WHERE can find a cat that is over four years old or whose name begins with the letter M. While this database is very simple and may not seem directly germane to data science, the skills that are learned can be applied to data science. For example, finding a product over a certain number of units or a customer over a certain age, or finding products that begin with a particular letter.
<br /><br />
One of the key aspects of programming with SQL is that that the commands always work the same way regardless of the data.

## Instructions

### Set Up
* Fork and Clone the Repo
* Install packages and enter virtual environment
    * `pipenv install`
    * `pipenv shell`

### Getting Started

For this part of the lesson, we'll use the Northwind database, the ERD (Entity Relationship Diagram) of which is shown below:

![ERM diagram of the Northwind database](/assets/erm-data-orders.png)

First, in `main.py`, we need to connect to a SQLite database using the Python sqlite3 library, then display the contents of the employees table:

```python
import sqlite3 
import pandas as pd

conn = sqlite3.connect('data.sqlite')

employees = pd.read_sql("""
SELECT *
  FROM employees;
""", conn)

print(employees)
```

Output:

| #   | employeeNumber | lastName  | firstName | extension | email                        | officeCode | reportsTo | jobTitle             |
|-----|----------------|-----------|-----------|-----------|------------------------------|------------|-----------|-----------------------|
| 0   | 1002           | Murphy    | Diane     | x5800     | dmurphy@classicmodelcars.com | 1          |           | President             |
| 1   | 1056           | Patterson | Mary      | x4611     | mpatterso@classicmodelcars.com | 1        | 1002      | VP Sales              |
| 2   | 1076           | Firrelli  | Jeff      | x9273     | jfirrelli@classicmodelcars.com | 1        | 1002      | VP Marketing          |
| 3   | 1088           | Patterson | William   | x4871     | wpatterson@classicmodelcars.com | 6        | 1056      | Sales Manager (APAC)  |
| 4   | 1102           | Bondur    | Gerard    | x5408     | gbondur@classicmodelcars.com | 4          | 1056      | Sale Manager (EMEA)   |
| 5   | 1143           | Bow       | Anthony   | x5428     | abow@classicmodelcars.com    | 1          | 1056      | Sales Manager (NA)    |
| 6   | 1165           | Jennings  | Leslie    | x3219     | ljennings@classicmodelcars.com | 1        | 1143      | Sales Rep             |
| 7   | 1166           | Thompson  | Leslie    | x4065     | lthompson@classicmodelcars.com | 1        | 1143      | Sales Rep             |
| 8   | 1188           | Firrelli  | Julie     | x2173     | jfirrelli@classicmodelcars.com | 2        | 1143      | Sales Rep             |
| 9   | 1216           | Patterson | Steve     | x4334     | spatterson@classicmodelcars.com | 2        | 1143      | Sales Rep             |
| 10  | 1286           | Tseng     | Foon Yue  | x2248     | ftseng@classicmodelcars.com  | 3          | 1143      | Sales Rep             |
| 11  | 1323           | Vanauf    | George    | x4102     | gvanauf@classicmodelcars.com | 3          | 1143      | Sales Rep             |
| 12  | 1337           | Bondur    | Loui      | x6493     | lbondur@classicmodelcars.com | 4          | 1102      | Sales Rep             |
| 13  | 1370           | Hernandez | Gerard    | x2028     | ghernande@classicmodelcars.com | 4        | 1102      | Sales Rep             |
| 14  | 1401           | Castillo  | Pamela    | x2759     | pcastillo@classicmodelcars.com | 4        | 1102      | Sales Rep             |
| 15  | 1501           | Bott      | Larry     | x2311     | lbott@classicmodelcars.com   | 7          | 1102      | Sales Rep             |
| 16  | 1504           | Jones     | Barry     | x102      | bjones@classicmodelcars.com  | 7          | 1102      | Sales Rep             |
| 17  | 1611           | Fixter    | Andy      | x101      | afixter@classicmodelcars.com | 6          | 1088      | Sales Rep             |
| 18  | 1612           | Marsh     | Peter     | x102      | pmarsh@classicmodelcars.com  | 6          | 1088      | Sales Rep             |
| 19  | 1619           | King      | Tom       | x103      | tking@classicmodelcars.com   | 6          | 1088      | Sales Rep             |
| 20  | 1621           | Nishi     | Mami      | x101      | mnishi@classicmodelcars.com  | 5          | 1056      | Sales Rep             |
| 21  | 1625           | Kato      | Yoshimi   | x102      | ykato@classicmodelcars.com   | 5          | 1621      | Sales Rep             |
| 22  | 1702           | Gerard    | Martin    | x2312     | mgerard@classicmodelcars.com | 4          | 1102      | Sales Rep             |

***Database output for employees table***

When filtering data using WHERE, you are trying to find rows that match a specific condition. The simplest condition involves checking whether a specific column contains a specific value. In SQLite, this is done using =, which is similar to == in Python:

```python
employees_named_patterson = pd.read_sql("""
SELECT *
  FROM employees
 WHERE lastName = "Patterson";
""", conn)

print(employees_named_patterson)
```

Output:

| #   | employeeNumber | lastName  | firstName | extension | email                        | officeCode | reportsTo | jobTitle             |
|-----|----------------|-----------|-----------|-----------|------------------------------|------------|-----------|-----------------------|
| 0   | 1056           | Patterson | Mary      | x4611     | mpatterso@classicmodelcars.com | 1        | 1002      | VP Sales              |
| 1   | 1088           | Patterson | William   | x4871     | wpatterson@classicmodelcars.com | 6        | 1056      | Sales Manager (APAC)  |
| 2   | 1216           | Patterson | Steve     | x4334     | spatterson@classicmodelcars.com | 2        | 1143      | Sales Rep             |

***Employee Data Output with WHERE filtering***

> Note: We are selecting all columns (SELECT *) but are no longer selecting all rows.  Instead, we are only selecting the 3 rows where the value of lastName is "Patterson". SQL is essentially doing something like this:

```python
# Selecting all of the records in the database
result = pd.read_sql("SELECT * FROM employees;", conn)
# Create a list to store the records that match the query
employees_named_patterson = []
# Loop over all of the employees
for _, data in result.iterrows():
    # Check if the last name is "Patterson"
    if data["lastName"] == "Patterson":
        # Add to list
        employees_named_patterson.append(data)

# Display the result list as a DataFrame
print(pd.DataFrame(employees_named_patterson))
```

Output:

| #   | employeeNumber | lastName  | firstName | extension | email                        | officeCode | reportsTo | jobTitle             |
|-----|----------------|-----------|-----------|-----------|------------------------------|------------|-----------|-----------------------|
| 1   | 1056           | Patterson | Mary      | x4611     | mpatterso@classicmodelcars.com | 1        | 1002      | VP Sales              |
| 3   | 1088           | Patterson | William   | x4871     | wpatterson@classicmodelcars.com | 6        | 1056      | Sales Manager (APAC)  |
| 9   | 1216           | Patterson | Steve     | x4334     | spatterson@classicmodelcars.com | 2        | 1143      | Sales Rep             |

***Employee Data Output with SELECT***

Except SQL is designed specifically to perform these kinds of queries efficiently! Even if you are pulling data from SQL into Python for further analysis, ```SELECT * FROM <table>;``` is very rarely the most efficient approach. You should be thinking about how to get SQL to do the "heavy lifting" for you in terms of selecting, filtering, and transforming the raw data!
<br /><br />
You can also combine WHERE clauses with SELECT statements other than SELECT * in order to filter rows and columns at the same time. For example:

```python
employees_named_patterson = pd.read_sql("""
SELECT firstName, lastName, email
  FROM employees
 WHERE lastName = "Patterson";
""", conn)

print(employees_named_patterson)
```

Output:

| #   | firstName | lastName  | email                         |
|-----|-----------|-----------|-------------------------------|
| 0   | Mary      | Patterson | mpatterso@classicmodelcars.com |
| 1   | William   | Patterson | wpatterson@classicmodelcars.com |
| 2   | Steve     | Patterson | spatterson@classicmodelcars.com |

***Employee Data Output with combined WHERE and SELECT filtering***

WHERE clauses are especially powerful when combined with more-complex SELECT statements. Most of the time you will want to use aliases (with AS) in the SELECT statements to make the WHERE clauses more concise and readable.

### Step 1: Selecting Employees Based on String Conditions

If we wanted to select all employees with 5 letters in their first name, that would look like this:

```python
pd.read_sql("""
SELECT *, length(firstName) AS name_length
  FROM employees
 WHERE name_length = 5;
""", conn)
```

Output:

| #   | employeeNumber | lastName  | firstName | extension | email                        | officeCode | reportsTo | jobTitle   | name_length |
|-----|----------------|-----------|-----------|-----------|------------------------------|------------|-----------|-------------|-------------|
| 0   | 1002           | Murphy    | Diane     | x5800     | dmurphy@classicmodelcars.com | 1          |           | President   | 5           |
| 1   | 1188           | Firrelli  | Julie     | x2173     | jfirrelli@classicmodelcars.com | 2        | 1143      | Sales Rep   | 5           |
| 2   | 1216           | Patterson | Steve     | x4334     | spatterson@classicmodelcars.com | 2        | 1143      | Sales Rep   | 5           |
| 3   | 1501           | Bott      | Larry     | x2311     | lbott@classicmodelcars.com   | 7          | 1102      | Sales Rep   | 5           |
| 4   | 1504           | Jones     | Barry     | x102      | bjones@classicmodelcars.com  | 7          | 1102      | Sales Rep   | 5           |
| 5   | 1612           | Marsh     | Peter     | x102      | pmarsh@classicmodelcars.com  | 6          | 1088      | Sales Rep   | 5           |

***Data Output: All Employees with First Name 5 letters***

Or, to select all employees with the first initial of "L", that would look like this:

```python
employees_with_l_names = pd.read_sql("""
SELECT *, substr(firstName, 1, 1) AS first_initial
  FROM employees
 WHERE first_initial = "L";
""", conn)

print(employees_with_l_names)
```

Output:

| #   | employeeNumber | lastName  | firstName | extension | email                        | officeCode | reportsTo | jobTitle   | first_initial |
|-----|----------------|-----------|-----------|-----------|------------------------------|------------|-----------|-------------|----------------|
| 0   | 1165           | Jennings  | Leslie    | x3291     | ljennings@classicmodelcars.com | 1        | 1143      | Sales Rep   | L              |
| 1   | 1166           | Thompson  | Leslie    | x4065     | lthompson@classicmodelcars.com | 1        | 1143      | Sales Rep   | L              |
| 2   | 1337           | Bondur    | Loui      | x6493     | lbondur@classicmodelcars.com | 4          | 1102      | Sales Rep   | L              |
| 3   | 1501           | Bott      | Larry     | x2311     | lbott@classicmodelcars.com   | 7          | 1102      | Sales Rep   | L              |

***Data Output using SELECT employees with first initial "L"***

> Important note: Just like in Python, you can compare numbers in SQL just by typing the number (e.g. name_length = 5) but if you want to compare to a string value, you need to surround the value with quotes (e.g. first_initial = "L"). If you forget the quotes, you will get an error, because SQL will interpret it as a variable name rather than a hard-coded value:

```python
pd.read_sql("""
SELECT *, substr(firstName, 1, 1) AS first_initial
  FROM employees
 WHERE first_initial = L;
""", conn)
```

Output:

```
---------------------------------------------------------------------------

OperationalError                          Traceback (most recent call last)

~/opt/anaconda3/envs/learn-env/lib/python3.8/site-packages/pandas/io/sql.py in execute(self, *args, **kwargs)
   2017         try:
-> 2018             cur.execute(*args, **kwargs)
   2019             return cur


OperationalError: no such column: L


The above exception was the direct cause of the following exception:


DatabaseError                             Traceback (most recent call last)

<ipython-input-7-083650d31057> in <module>
----> 1 pd.read_sql("""
      2 SELECT *, substr(firstName, 1, 1) AS first_initial
      3   FROM employees
      4  WHERE first_initial = L;
      5 """, conn)


~/opt/anaconda3/envs/learn-env/lib/python3.8/site-packages/pandas/io/sql.py in read_sql(sql, con, index_col, coerce_float, params, parse_dates, columns, chunksize)
    562 
    563     if isinstance(pandas_sql, SQLiteDatabase):
--> 564         return pandas_sql.read_query(
    565             sql,
    566             index_col=index_col,


~/opt/anaconda3/envs/learn-env/lib/python3.8/site-packages/pandas/io/sql.py in read_query(self, sql, index_col, coerce_float, params, parse_dates, chunksize, dtype)
   2076 
   2077         args = _convert_params(sql, params)
-> 2078         cursor = self.execute(*args)
   2079         columns = [col_desc[0] for col_desc in cursor.description]
   2080 


~/opt/anaconda3/envs/learn-env/lib/python3.8/site-packages/pandas/io/sql.py in execute(self, *args, **kwargs)
   2028 
   2029             ex = DatabaseError(f"Execution failed on sql '{args[0]}': {exc}")
-> 2030             raise ex from exc
   2031 
   2032     @staticmethod


DatabaseError: Execution failed on sql '
SELECT *, substr(firstName, 1, 1) AS first_initial
  FROM employees
 WHERE first_initial = L;
': no such column: L
```

### Step 2: Selecting Order Details Based on Price

Below we select all order details where the price each, rounded to the nearest integer, is 30 dollars:

```python
thirty_dollar_orders = pd.read_sql("""
SELECT *, CAST(round(priceEach) AS INTEGER) AS rounded_price_int
  FROM orderDetails
 WHERE rounded_price_int = 30;
""", conn)

print(thirty_dollar_orders)
```

Output:

| #   | orderNumber | productCode | quantityOrdered | priceEach | orderLineNumber | rounded_price_int |
|-----|-------------|-------------|------------------|-----------|------------------|--------------------|
| 0   | 10104       | S24_2840    | 44               | 30.41     | 10               | 30                 |
| 1   | 10173       | S24_1937    | 31               | 29.87     | 9                | 30                 |
| 2   | 10184       | S24_2840    | 42               | 30.06     | 7                | 30                 |
| 3   | 10280       | S24_1937    | 20               | 29.87     | 12               | 30                 |
| 4   | 10332       | S24_1937    | 45               | 29.87     | 6                | 30                 |
| 5   | 10367       | S24_1937    | 23               | 29.54     | 13               | 30                 |
| 6   | 10380       | S24_1937    | 32               | 29.87     | 4                | 30                 |

***Output with SELECT order details at. rounded price***

### Step 3: Selecting Orders Based on Date

We can use the strftime function to select all orders placed in January of any year:

```python
january_orders = pd.read_sql("""
SELECT *, strftime("%m", orderDate) AS month
  FROM orders
 WHERE month = "01";
""", conn)

print(january_orders)
```

Output:

| #   | orderNumber | orderDate  | requiredDate | shippedDate | status   | comments                                         | customerNumber | month |
|-----|-------------|------------|--------------|-------------|----------|--------------------------------------------------|----------------|--------|
| 0   | 10100       | 2003-01-06 | 2003-01-13   | 2003-01-10  | Shipped  |                                                  | 363            | 01     |
| 1   | 10101       | 2003-01-09 | 2003-01-18   | 2003-01-11  | Shipped  | Check on availability.                          | 128            | 01     |
| 2   | 10102       | 2003-01-10 | 2003-01-18   | 2003-01-14  | Shipped  |                                                  | 181            | 01     |
| 3   | 10103       | 2003-01-29 | 2003-02-07   | 2003-02-02  | Shipped  |                                                  | 121            | 01     |
| 4   | 10104       | 2003-01-31 | 2003-02-09   | 2003-02-01  | Shipped  |                                                  | 141            | 01     |
| 5   | 10208       | 2004-01-02 | 2004-01-11   | 2004-01-04  | Shipped  |                                                  | 146            | 01     |
| 6   | 10209       | 2004-01-09 | 2004-01-15   | 2004-01-12  | Shipped  |                                                  | 347            | 01     |
| 7   | 10210       | 2004-01-12 | 2004-01-22   | 2004-01-20  | Shipped  |                                                  | 177            | 01     |
| 8   | 10211       | 2004-01-15 | 2004-01-25   | 2004-01-18  | Shipped  |                                                  | 406            | 01     |
| 9   | 10212       | 2004-01-16 | 2004-01-24   | 2004-01-18  | Shipped  |                                                  | 141            | 01     |
| 10  | 10213       | 2004-01-22 | 2004-01-28   | 2004-01-27  | Shipped  | Difficult to negotiate with customer. We need... | 489            | 01     |
| 11  | 10214       | 2004-01-26 | 2004-02-04   | 2004-01-29  | Shipped  |                                                  | 458            | 01     |
| 12  | 10215       | 2004-01-29 | 2004-02-08   | 2004-02-01  | Shipped  | Customer requested that FedEx Ground is used...  | 475            | 01     |
| 13  | 10362       | 2005-01-05 | 2005-01-16   | 2005-01-10  | Shipped  |                                                  | 161            | 01     |
| 14  | 10363       | 2005-01-06 | 2005-01-12   | 2005-01-10  | Shipped  |                                                  | 334            | 01     |
| 15  | 10364       | 2005-01-06 | 2005-01-17   | 2005-01-09  | Shipped  |                                                  | 350            | 01     |
| 16  | 10365       | 2005-01-07 | 2005-01-18   | 2005-01-11  | Shipped  |                                                  | 320            | 01     |
| 17  | 10366       | 2005-01-10 | 2005-01-19   | 2005-01-12  | Shipped  |                                                  | 381            | 01     |
| 18  | 10367       | 2005-01-12 | 2005-01-21   | 2005-01-16  | Resolved | This order was disputed and resolved on 2/1/20...| 205            | 01     |
| 19  | 10368       | 2005-01-19 | 2005-01-27   | 2005-01-24  | Shipped  | Can we renegotiate this one?                    | 124            | 01     |
| 20  | 10369       | 2005-01-20 | 2005-01-28   | 2005-01-24  | Shipped  |                                                  | 379            | 01     |
| 21  | 10370       | 2005-01-20 | 2005-02-01   | 2005-01-25  | Shipped  |                                                  | 276            | 01     |
| 22  | 10371       | 2005-01-23 | 2005-02-03   | 2005-01-25  | Shipped  |                                                  | 124            | 01     |
| 23  | 10372       | 2005-01-26 | 2005-02-05   | 2005-01-28  | Shipped  |                                                  | 398            | 01     |
| 24  | 10373       | 2005-01-31 | 2005-02-08   | 2005-02-06  | Shipped  |                                                  | 311            | 01     |

***Data Output using strftime function***

We can also check to see if any orders were shipped late (shippedDate after requiredDate, i.e. the number of days late is a positive number):

```python
late_orders = pd.read_sql("""
SELECT *, julianday(shippedDate) - julianday(requiredDate) AS days_late
  FROM orders
 WHERE days_late > 0;
""", conn)

print(late_orders)
```

Output: 
| #   | orderNumber | orderDate  | requiredDate | shippedDate | status   | comments                                                                 | customerNumber | days_late |
|-----|-------------|------------|---------------|-------------|----------|---------------------------------------------------------------------------|----------------|-----------|
| 0   | 10165       | 2003-10-22 | 2003-10-31    | 2003-12-26  | Shipped  | This order was on hold because customers's credit limit was exceeded.    | 148            | 56.0      |

***Data Output for Orders Shipped Late***

That was the last query in this lesson using the Northwind data, so let's close that connection at the end of the file.

```python
conn.close()
```

## Considerations

### Conditional Operators in SQL

In all of the above queries, we used the = operator to check if we had an exact match for a given value. However, what if you wanted to select the order details where the price was at least 30 dollars? Or all of the orders that don't currently have a shipped date? We'll need some more advanced conditional operators for that.
<br /><br />
Some important ones to know are:
* `!=` ("not equal to") - Similar to not combined with `==` in Python
* `>` ("greater than") - Similar to `>` in Python
* `>=` ("greater than or equal to") - Similar to `>=` in Python
* `<` ("less than") - Similar to `<` in Python
* `<=` ("less than or equal to") - Similar to `<=` in Python
* `AND` - Similar to `and` in Python
* `OR` - Similar to `or` in Python
* `BETWEEN` - Similar to placing a value between two values with `<=` and `and` in Python, e.g. (`2 <= x`) and (`x <= 5`)
* `IN` - Similar to `in` in Python
* `LIKE` - Uses wildcards to find similar strings. No direct equivalent in Python, but similar to some Bash terminal commands.
