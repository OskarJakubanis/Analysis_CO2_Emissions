## pandas as pd

pd.read\_sql\_query(sql\_query, conn) – executes a SQL query on a connected database and returns the results as a pandas DataFrame
df.to\_csv(filepath, index=True/False, header=True/False) – saves a pandas DataFrame to a CSV file with options to include/exclude index and column headers
df.rename(columns=dict, inplace=True) – renames columns in a DataFrame using a dictionary mapping; inplace=True modifies the original DataFrame
df.groupby(by)\[column].sum() – groups data by one or more columns and calculates the sum of the selected column within groups
df.groupby(by)\[column].mean() – groups data by one or more columns and calculates the mean of the selected column within groups
df\['column'].isin(values) – filters DataFrame rows where the column values are in the specified list
df\['column'].notnull() – filters rows where the column values are not null
df\['column'].isnull() – filters rows where the column values are null
series.astype(dtype) – converts elements of a Series to the specified data type
df.sort\_values(by, ascending=True/False) – sorts DataFrame by a column or list of columns in ascending or descending order
DataFrame.LAG() / DataFrame.MAX() / DataFrame.MIN() – SQL window functions and aggregate functions executed through SQL queries

## SQLite3

sqlite3.connect(database) – opens a connection to a SQLite database file; returns a connection object
connection.cursor() – creates a cursor object to execute SQL commands on the database
cursor.execute(sql\_query) – executes an SQL query using the cursor
connection.commit() – commits any changes made to the database (INSERT, UPDATE, DELETE)
connection.close() – closes the database connection and releases resources
pd.read\_sql\_query(sql\_query, connection) – executes SQL query via pandas and returns a DataFrame (requires sqlite3 connection)
cursor.fetchall() – fetches all rows from the last executed query
cursor.fetchone() – fetches the next row from the last executed query
connection.rollback() – rolls back any uncommitted changes in case of errors
