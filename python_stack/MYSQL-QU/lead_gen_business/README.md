# Lead Gen Business - SQL Analysis

## Project Overview
This project involves performing deep data analysis on a Lead Generation Business database. The goal is to extract meaningful insights such as revenue trends, client site performance, and lead generation metrics using MySQL.

## Key SQL Concepts Applied
* **Multi-table Joins:** Connecting clients, sites, billing, and leads.
* **Aggregate Functions:** `SUM()` for revenue and `COUNT()` for leads/sites.
* **Data Grouping:** Advanced use of `GROUP BY` and `GROUP_CONCAT`.
* **Date Filtering:** Filtering records within specific years and months.
* **Ordering:** Sorting results for better readability and reporting.

## Database Structure
The database follows a relational model where:
- A **Client** can have multiple **Sites** and **Billing** records.
- Each **Site** generates multiple **Leads**.