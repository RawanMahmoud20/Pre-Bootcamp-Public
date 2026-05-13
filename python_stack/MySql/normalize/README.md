# Assignment: Normalization Implementation

## Project Overview
This project focuses on refining a database schema to adhere to the three forms of normalization. Based on the wireframe in **image_2bed75.png**, the original schema for tracking students and their interests was inefficient and violated database design principles.

## Normalization Steps Taken
1. **First Normal Form (1NF)**: Removed the `interests` text field from the `students` table to avoid storing multiple values in a single column.
2. **Second & Third Normal Forms**: Organized attributes so that each table represents a single entity and removed transitive dependencies.
3. **Many-to-Many Relationship**: Created a join table (`student_interests`) to allow multiple students to be associated with multiple interests efficiently.

## Technical Details
- **Schema**: 4 Tables (`dojos`, `students`, `interests`, `student_interests`).
- **Constraints**: Utilized `FOREIGN KEY` with `ON DELETE CASCADE` to maintain referential integrity.
- **Engine**: MySQL.

## How to use
Run the provided SQL script to generate the normalized database structure. This design ensures data consistency and minimizes redundancy.