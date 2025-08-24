# CO₂ Emissions Analysis (2000–2024)

## Project Overview

This project examines global CO₂ emissions using datasets from Our World in Data. It focuses on analyzing total emissions, per capita emissions, and absolute changes across countries and regions.

## Analysis Goals

The goal is to identify countries with the largest increases or reductions in emissions and to track trends in the three most populous nations. All analyses are performed using SQL queries applied to the downloaded datasets. The following analyses were performed:

* Countries with the largest reduction in total emissions (2000–2024)
* Countries with the largest increase in total emissions (2000–2024)
* Countries with the largest reduction in per capita emissions (2000–2024)
* Countries with the largest increase in per capita emissions (2000–2024)
* Largest absolute changes (in tons of CO₂)
* The 3 most populous countries and their emissions changes

## Data

Two datasets were used, both downloaded from Our World in Data:

1. **`owid-co2-data.csv`** – main file containing:

   * `country` – country name
   * `year` – year
   * `co2` – total CO₂ emissions in tons
   * `population` – population (used for per capita calculations)
   * other indicators, e.g., emissions by sector, which can be used for extended analyses

2. **`population.csv`** – additional dataset with population (just population numbers), used for comparison or verification with OWID data.

All calculations were done manually in SQL based on the datasets, computing percentage and absolute changes, as well as per capita values.
