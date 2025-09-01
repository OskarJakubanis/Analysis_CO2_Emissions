# 📊 CO₂ Emissions Analysis (2000–2024)

This project provides an analytical pipeline to explore, summarize, and export CO₂ emissions data across countries from 2000 to 2024. The dataset is sourced from **Our World in Data**.  
This report is a key tool for CO₂ analysis, allowing for subsequent examination of individual countries to identify which nations others can learn from, which countries should diligently follow these lessons, and which economic sectors need transformation. While change is not immediate, modern technology enables us to implement it more effectively.

---

## 🎯 Objectives

* Identify countries with the largest increases and decreases in CO₂ emissions.
* Calculate absolute and percentage changes in CO₂ emissions between 2000 and 2024.
* Analyze the relationship between population size and CO₂ emissions.
* Export insights into CSV reports for further analysis.  

---

## ⚙️ Technologies Used

* Python 3.9+
* `sqlite3` for database connection and SQL queries

📁 Required libraries are listed in [`requirements.txt`](./requirements.txt)  
📖 Function-level usage is documented in [`used_functions.md`](./used_functions.md)

---

## 📁 Script Overview

The pipeline is designed to efficiently handle data operations, from initial loading and validation to automated analysis and reporting:  
  * Imported `owid-co2-data.csv` into SQLite and materialized the `emissions` table.  
  * Validated schema and data quality: enforced numeric types for `co2`, `population`, and `year`; checked NULLs/missing values; standardized key fields.  
  * Persisted the database as **`ANALYSIS_CO2.db`**. This file is the base for all SQL automation in Python.
  * Python scripts connect to **`ANALYSIS_CO2.db`** and execute SQL queries using `pandas.read_sql_query`.
  * Queries include filtering, CTEs, and window functions to calculate absolute and relative CO₂ changes.
  * Results are exported to multiple CSV reports:

    * Top 100 growth (percent and nominal)
    * Top 100 decline (percent and nominal)
    * Top 100 most populous countries with CO₂ changes

> **Note:** The pipeline is reusable: as long as the base CSV keeps the same filename and column names, you can refresh the DB and re-run the scripts on a schedule.

---

## 🧪 Project Workflow

1. **Review the data** – check `data_description.md` to understand the structure and content of the CSV files.
2. **Clone the repository** to your local machine.
3. **Run the analysis script (`.py`)** – generate CO₂ emissions reports and export results to CSV files.
4. **Check the console output** – review printed metrics and any generated files for insights.

*In `.py` file, `#` comments show step-by-step procedures.*

---

## 📬 Contact

For questions, suggestions, or collaboration proposals, please [open an issue](https://github.com/your-repo/issues) or contact me directly.
