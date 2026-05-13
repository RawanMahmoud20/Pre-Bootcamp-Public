# Belt Certifications Database Design

This project implements a relational schema for tracking student belt achievements, as seen in **image_2d04f1.png**.

## 1. Database Tables Analysis
- **Students Table**: Stores unique names of participants.
- **Belts Table**: Stores the different belt levels (Yellow, Red, Black).
- **Student_Belts Table**: A many-to-many join table that maps students to their earned certifications.

## 2. Relationships & Logic
- **Many-to-Many**: Since one student can have multiple belts and one belt can belong to many students, a bridge table is required to normalize the data.
- **Data Integrity**: Using `ON DELETE CASCADE` ensures that if a student or belt type is removed, the associated records in the bridge table are automatically cleaned up.

## 3. Schema Summary
| Entity | Relationship | Target Entity | Type |
| :--- | :--- | :--- | :--- |
| Student | Earns | Belts | Many-to-Many |

> **Summary**: This design prevents data duplication and allows for efficient querying (e.g., finding all students with a Black belt or listing all belts for a specific student).
