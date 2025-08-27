# 📊 CO₂ Emissions Analysis (2000–2024)

This project provides an analytical pipeline to explore, summarize, and export CO₂ emissions data across countries from 2000 to 2024. The dataset is sourced from **Our World in Data**.

---

## 🎯 Objectives

* Identify countries with the largest increases and decreases in CO₂ emissions.
* Calculate absolute and percentage changes in CO₂ emissions between 2000 and 2024.
* Analyze the relationship between population size and CO₂ emissions.
* Export insights into CSV reports for further analysis.

---

## 🧾 Data Sources

* `emissions.db` – SQLite database containing CO₂ emissions, population, and year-by-country records from Our World in Data.

---

## ⚙️ Technologies Used

* Python 3.9+
* `pandas` for data manipulation and SQL queries
* `sqlite3` for database connection and querying

📁 Required libraries are listed in [`requirements.txt`](./requirements.txt)
📖 Function-level usage is documented in [`used_functions.md`](./used_functions.md)

---

## 📁 Script Overview

* Scripts manage data provided in `emissions.csv`.

* Python scripts process the query results through filtering, aggregation, window functions, and conditional calculations for growth and decline metrics, and export multiple CSV files including:

  * Top 10 growth in percent and nominal
  * Top 10 decline in percent and nominal
  * Top 10 most populous countries with CO₂ changes

* SQL queries are written and executed within Python using `pandas.read_sql_query` and `sqlite3` connection objects.

---

## 🧪 Project Workflow

1. **Review the data** – check `data_description.md` to understand the structure and content of the CSV files.
2. **Clone the repository** – download all project files to your local machine.
3. **Run the analysis script (`.py`)** – generate CO₂ emissions reports and export results to CSV files.
4. **Check the console output** – review printed metrics and any generated files for insights.

*Refer to `used_functions.md` for an overview of key Python and library functions used.*  
*In `.py` files, `#` comments show step-by-step procedures.*

---

## 📬 Contact

For questions, suggestions, or collaboration proposals, please [open an issue](https://github.com/your-repo/issues) or contact me directly.
