# World Queries - MySQL Exploration

## Project Overview
This repository contains a collection of SQL queries executed on the relational `world` database. The project explores global data, extracting specific insights regarding country populations, official languages, city distributions, and government structures.

## Technical Skills Applied
* **Relational Database Joins:** Connecting country profiles with local cities and languages spoken.
* **Complex Data Filtering:** Utilizing specific numeric and text constraints (`Population`, `SurfaceArea`, `Percentage`).
* **Aggregate Reporting:** Grouping and counting global geographical data using `COUNT()` and `GROUP BY`.
* **Sorting Efficiency:** Implementing structured output using `ORDER BY`.

## Database Entities
* `countries`: Global metrics like GNP, life expectancy, population, and government type.
* `cities`: Individual city logs mapped via country codes.
* `languages`: Text records capturing global dialects and their usage percentages.