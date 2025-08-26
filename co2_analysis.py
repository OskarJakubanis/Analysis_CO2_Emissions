import sqlite3
import pandas as pd

# 1. Połączenie z bazą danych
conn = sqlite3.connect(r"C:\Users\Dell\Downloads\population\ANALYSIS_CO2.db")

# 2. Top 10 wzrostów CO2 (2000 -> 2023)
query_growth = """
WITH filtered AS (
    SELECT country,
           year,
           CAST(co2 AS REAL) AS co2
    FROM emissions
    WHERE year IN (2000, 2023)
      AND country IS NOT NULL
      AND co2 IS NOT NULL
),
growth AS (
    SELECT
        country,
        year,
        co2,
        LAG(co2) OVER (PARTITION BY country ORDER BY year) AS co2_2000,
        (co2 / LAG(co2) OVER (PARTITION BY country ORDER BY year)) - 1 AS co2_growth_ratio
    FROM filtered
)
SELECT country,
       co2_2000,
       co2 AS co2_2023,
       ROUND(co2_growth_ratio * 100, 2) AS co2_growth_pct
FROM growth
WHERE year = 2023 AND co2_growth_ratio IS NOT NULL
ORDER BY co2_growth_ratio DESC
LIMIT 100;
"""
df_growth = pd.read_sql_query(query_growth, conn)
df_growth.to_csv("top10_growth.csv", index=False)

# 2b. Top 10 wzrostów nominalnych CO2 (2023 - 2000)
query_nominal_growth = """
WITH filtered AS (
    SELECT country,
           year,
           CAST(co2 AS REAL) AS co2
    FROM emissions
    WHERE year IN (2000, 2023)
      AND country IS NOT NULL
      AND co2 IS NOT NULL
),
growth AS (
    SELECT
        country,
        year,
        co2,
        LAG(co2) OVER (PARTITION BY country ORDER BY year) AS co2_2000,
        co2 - LAG(co2) OVER (PARTITION BY country ORDER BY year) AS co2_change_abs
    FROM filtered
)
SELECT country,
       co2_2000,
       co2 AS co2_2023,
       co2_change_abs
FROM growth
WHERE year = 2023 AND co2_change_abs IS NOT NULL
ORDER BY co2_change_abs DESC
LIMIT 100;
"""
df_nominal_growth = pd.read_sql_query(query_nominal_growth, conn)
df_nominal_growth.to_csv("top10_growth_nominal.csv", index=False)

# 2c. Top 10 spadków nominalnych CO2
query_nominal_decline = query_nominal_growth.replace("DESC", "ASC")
df_nominal_decline = pd.read_sql_query(query_nominal_decline, conn)
df_nominal_decline.to_csv("top10_decline_nominal.csv", index=False)

# 3. Top 10 spadków CO2 (2000 -> 2023)
query_decline = query_growth.replace("DESC", "ASC")
df_decline = pd.read_sql_query(query_decline, conn)
df_decline.to_csv("top10_decline.csv", index=False)

# 4. Top 10 najbardziej zaludnionych krajów w 2023 + zmiany CO2
query_top10_pop = """
WITH pop2023 AS (
    SELECT country,
           CAST(population AS REAL) AS population
    FROM emissions
    WHERE year = 2023 AND population IS NOT NULL
),
co2data AS (
    SELECT country,
           year,
           CAST(co2 AS REAL) AS co2
    FROM emissions
    WHERE year IN (2000, 2023)
      AND co2 IS NOT NULL
)
SELECT p.country,
       p.population,
       MAX(CASE WHEN c.year = 2000 THEN c.co2 END) AS co2_2000,
       MAX(CASE WHEN c.year = 2023 THEN c.co2 END) AS co2_2023,
       (MAX(CASE WHEN c.year = 2023 THEN c.co2 END) -
        MAX(CASE WHEN c.year = 2000 THEN c.co2 END)) AS co2_change_abs,
       ROUND(((MAX(CASE WHEN c.year = 2023 THEN c.co2 END) * 1.0 /
               MAX(CASE WHEN c.year = 2000 THEN c.co2 END)) - 1) * 100, 2) AS co2_change_pct
FROM pop2023 p
LEFT JOIN co2data c ON p.country = c.country
GROUP BY p.country, p.population
ORDER BY p.population DESC
LIMIT 100;
"""
df_top10_pop = pd.read_sql_query(query_top10_pop, conn)
df_top10_pop.to_csv("top10_population_co2.csv", index=False)

# 5. Zamknięcie połączenia
conn.close()
