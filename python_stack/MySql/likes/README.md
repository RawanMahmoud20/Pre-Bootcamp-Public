# Likes System Database Design

## Description
This project focuses on designing a relational database for a social media "Like" feature. The primary goal was to handle the **Many-to-Many** relationship between Users and Posts effectively through a join table (`likes`).

## Database Structure
The design includes:
- **users**: Identity of the people using the app.
- **posts**: The content created by users.
- **likes**: A middle table that records which user liked which post, ensuring data integrity.

## Key Learning Points
- Implementing **Many-to-Many** relationships.
- Using **Singular Naming Convention** for foreign keys (e.g., `user_id` instead of `users_id`).
- Cascading deletes to ensure that if a post is deleted, its likes are also removed.

## How to use
Run the provided SQL script in your database management tool (like MySQL Workbench) to generate the schema and test the data relationships.