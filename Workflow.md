# Workflow: Data Exploration / Initial Steps

* Created a SQLite database named `ANALYSIS_CO2` using DB Browser for SQLite.
* Imported `owid-co2-data.csv` as the table `emissions`, marking the first row as column names.
* Used `SELECT *` to check available columns and decide which ones to include in analyses.
* Selected specific columns (`country`, `year`, `co2`, `population`, `co2_per_capita`) with commas separating them.
* Filtered out all `NULL` values to avoid empty rows and check for any missing or incorrect data.
* Restricted the data to years 2000–2025 using `WHERE year BETWEEN 2000 AND 2025`.
* Grouped by `country` and calculated averages using `AVG` to get per-country summaries.
* Performed a simple calculation for CO₂ per capita: `AVG(e.co2 / e.population)` as `co2_per_capita`.

```sql
SELECT e.country,
       AVG(e.co2) AS avg_co2,
       AVG(e.co2_per_capita) AS avg_co2_per_capita,
       AVG(e.population) AS avg_population,
       AVG(e.co2 / e.population) AS calculated_co2_per_capita
FROM emissions AS e
WHERE e.country IS NOT NULL
  AND e.year IS NOT NULL
  AND e.co2 IS NOT NULL
  AND e.population IS NOT NULL
  AND e.co2_per_capita IS NOT NULL
  AND e.year BETWEEN 2000 AND 2025
GROUP BY e.country;
```

* As a result, we have 227 rows representing countries or regions.
