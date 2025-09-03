# This script performs CO₂ emissions analysis for the period 2000–2023 and calculates top 100 countries with the highest
# 1. percent growth in CO₂ emissions
# 2. nominal growth in CO₂ emissions
# 3. nominal decline in CO₂ emissions
# 4. percent decline in CO₂ emissions
# 5. most populous countries in 2023 with their CO₂ changes

# Import necessary libraries:
import sqlite3                 # sqlite3: to connect to and manage the SQLite database
import pandas as pd            # pandas: to handle data analysis and transformations

# Connect to SQLite database file 'ANALYSIS_CO2.db' and create a connection object
conn = sqlite3.connect(r"C:\Users\Dell\Downloads\population\ANALYSIS_CO2.db")

# Create dataset "growth" to add four columns: co2_2000, co2_2023, co2_growth_pct, co2_growth_nominal
# Ensure country, co2, and year contain valid values (not NULL) to avoid missing data
query_growth_pct = """
WITH growth AS (
    SELECT
        country,
        population,
        MAX(CASE WHEN year = 2000 THEN CAST(co2 AS REAL) END) AS co2_2000,
        MAX(CASE WHEN year = 2023 THEN CAST(co2 AS REAL) END) AS co2_2023
    FROM emissions
    WHERE country IS NOT NULL
      AND co2 IS NOT NULL
      AND year IN (2000, 2023)
    GROUP BY country
)
SELECT
    country,
    population,
    co2_2000,
    co2_2023,
    ROUND((co2_2023 / co2_2000 - 1) * 100, 2) AS co2_growth_pct,
    ROUND((co2_2023 - co2_2000), 2) As co2_growth_nominal
FROM growth
ORDER BY co2_growth_pct DESC
LIMIT 100;
"""

# Top 100 percent growth in CO2 emissions (2000–2023) 
# Create a DataFrame from the SQL query results and export it to a CSV file
df_growth_pct = pd.read_sql_query(query_growth_pct, conn)
df_growth_pct.to_csv("top100_growth.csv", index=False, header=True)

# Top 100 percent decline in CO2 emissions (2000–2023) 
# Create a DataFrame from the SQL query results and export it to a CSV file
query_decline_pct = query_growth_pct.replace("DESC", "ASC")
df_decline_pct = pd.read_sql_query(query_decline_pct, conn)
df_decline_pct.to_csv("top100_decline.csv", index=False, header=True)

# Top 100 nominal growth in CO2 emissions (2000–2023) 
# Create a DataFrame from the SQL query results and export it to a CSV file
query_nominal_growth = query_growth_pct.replace("ORDER BY co2_growth_pct DESC", "ORDER BY co2_growth_nominal DESC")
df_nominal_growth = pd.read_sql_query(query_nominal_growth, conn)
df_nominal_growth.to_csv("top100_growth_nominal.csv", index=False, header=True)

# Top 100 nominal decline in CO2 emissions (2000–2023) 
# Create a DataFrame from the SQL query results and export it to a CSV file
query_nominal_decline = query_growth_pct.replace("ORDER BY co2_growth_pct DESC", "ORDER BY co2_growth_nominal ASC")
df_nominal_decline = pd.read_sql_query(query_nominal_decline, conn)
df_nominal_decline.to_csv("top100_decline_nominal.csv", index=False, header=True)

# Top 100 most populous countries in 2023 and CO2 changes (2000–2023) 
# Create a DataFrame from the SQL query results and export it to a CSV file
query_population = query_growth_pct.replace("ORDER BY co2_growth_pct DESC", "ORDER BY population DESC")
df_pop = pd.read_sql_query(query_population, conn)
df_pop.to_csv("top100_population_co2.csv", index=False, header=True)

# Close the database connection
conn.close()
