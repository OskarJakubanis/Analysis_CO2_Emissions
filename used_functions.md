## pandas as pd

**`pd.read_sql_query(sql_query, conn)`** – executes a SQL query on a connected database and returns the results as a pandas DataFrame  
**`df.to_csv(filepath, index, header)`** – saves a DataFrame to a CSV file with options to include/exclude index and column headers  
**`df.rename(columns=dict, inplace)`** – renames columns in a DataFrame using a dictionary mapping; `inplace=True` modifies the original DataFrame  
**`df.groupby(by)[column].sum()`** – groups data by one or more columns and calculates the sum of the selected column within groups  
**`df.groupby(by)[column].mean()`** – groups data by one or more columns and calculates the mean of the selected column within groups  
**`df['column'].isin(values)`** – filters DataFrame rows where the column values are in the specified list  
**`df['column'].notnull()`** – filters rows where the column values are not null  
**`df['column'].isnull()`** – filters rows where the column values are null  
**`series.astype(dtype)`** – converts elements of a Series to the specified data type  
**`df.sort_values(by, ascending)`** – sorts DataFrame by a column or list of columns in ascending or descending order  
**`DataFrame.LAG() / DataFrame.MAX() / DataFrame.MIN()`** – SQL window functions and aggregate functions executed through SQL queries  

## SQLite3

**`sqlite3.connect(database)`** – opens a connection to a SQLite database file; returns a connection object  
**`connection.cursor()`** – creates a cursor object to execute SQL commands on the database  
**`cursor.execute(sql_query)`** – executes an SQL query using the cursor  
**`connection.commit()`** – commits any changes made to the database (INSERT, UPDATE, DELETE)  
**`connection.close()`** – closes the database connection and releases resources  
**`pd.read_sql_query(sql_query, connection)`** – executes SQL query via pandas and returns a DataFrame  
**`cursor.fetchall()`** – fetches all rows from the last executed query  
**`cursor.fetchone()`** – fetches the next row from the last executed query  
**`connection.rollback()`** – rolls back any uncommitted changes to the last commit point  

## SQL Syntax & Functions

**`WITH`** – creates a Common Table Expression (CTE) `growth`  
**`SELECT`** – retrieves data from the database (used twice)  
**`MAX()`** – aggregate function(used here to pivot rows into columns by selecting the non-NULL value from a group)  
**`CASE WHEN`** – conditional expression  
**`CAST(co2 AS REAL)`** – data type conversion  
**`END`** – closes the CASE expression  
**`AS`** – assigns column aliases (`co2_2000`, `co2_2023`, `co2_growth_pct`, `co2_growth_nominal`)  
**`FROM`** – specifies the `emissions` table  
**`WHERE`** – filters rows based on conditions  
**`IS NOT NULL`** – excludes null values  
**`IN (2000, 2023)`** – filters for specific years  
**`GROUP BY`** – groups results by country  
**`ROUND(number, decimals)`** – rounds values to 2 decimal places  
**`ORDER BY`** – sorts results in descending order by percentage growth  
**`DESC`** – descending sort order  
**`LIMIT`** – limits results to 100 rows  
