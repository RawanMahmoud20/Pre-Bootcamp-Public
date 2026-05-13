# Food Reviews Database Design

This project demonstrates the transformation of a Food Review UI into a structured Relational Data Model.

## 1. Database Tables Analysis
Based on the wireframe in **image_2d171a.jpg**, the following entities were identified:
- **Users Table**: Stores reviewers' personal information.
- **Restaurants Table**: Stores restaurant details like name and images.
- **Reviews Table**: Acts as a bridge between users and restaurants.

## 2. Relationships & ERD Strategy
- **Many-to-Many Relationship**: A user can review multiple restaurants, and a restaurant can have reviews from multiple users. The `reviews` table serves as the join table.
- **Foreign Key Naming**: Adhering to standards, foreign keys are named in singular form: `user_id` and `restaurant_id`.
- **Data Normalization**: Restaurant data is separated from reviews to prevent redundancy.

## 3. Schema Summary
| Entity | Relationship | Target Entity | Type |
| :--- | :--- | :--- | :--- |
| User | Writes | Reviews | One-to-Many |
| Restaurant | Receives | Reviews | One-to-Many |

> **Note**: The "Stars" in the UI are stored as an integer `rating` field. The total review count is dynamically calculated using SQL aggregate functions (`COUNT`).