# Books Assignment: Logic & ERD Strategy

This project focuses on the **Many-to-Many** relationship between Users and Books through the "Favorite Books" feature.

## 1. Entities Analysis
Based on the requirements in **image_c019d5.png**:
- **Users**: Stores personal data of the readers.
- **Books**: Stores information about books (Title and Author).
- **Favorites**: A join table linking users to their preferred books.

## 2. Table Schema Details
- **Users Table**: Standard attributes (`id`, `first_name`, `last_name`, `email`).
- **Books Table**: Contains `title` and `author`. Note: The author is included directly to simplify the design as per assignment guidelines.
- **Favorites Table**: Contains two foreign keys: `user_id` and `book_id`.

## 3. Relationships
- **Many-to-Many**: 
    - One user can have many favorite books.
    - One book can be favorited by many users.
- To implement this, we use the `favorites` table to bridge the two main entities.

## 4. Naming Conventions
Following the best practices mentioned in related documents (like **image_2d171a.jpg**):
- Foreign keys are strictly named in **singular form** (`user_id`, `book_id`).

---
