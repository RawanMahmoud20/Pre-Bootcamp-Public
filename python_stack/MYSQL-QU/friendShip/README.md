# Friendships Assignment - SQL Self Join Practice

## Project Description
This assignment focuses on implementing a **Many-to-Many self-referencing relationship** in MySQL. The goal is to manage a social-media-like connection system where users can "friend" other users in the same database.

## Technical Objectives
* Database Schema Design from an ERD.
* Implementation of **SQL Self-Joins** using table aliases.
* Advanced data retrieval using `JOIN` and `LEFT JOIN` operations.
* Utilizing aggregate functions like `COUNT()` and grouping data with `GROUP BY`.

## Database Schema
The schema consists of two main tables:
1. `users`: Stores user profile information.
2. `friendships`: A join table that maps `user_id` to `friend_id`, both acting as foreign keys to the `users` table.