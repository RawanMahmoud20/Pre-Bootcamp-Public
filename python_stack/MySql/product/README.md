# Amazon Product Categories Database Design

This project covers the database implementation for a product categorization system, inspired by the Amazon UI in **image_2d0ff3.png**.

## 1. Database Tables Analysis
- **Categories**: Stores top-level classifications (e.g., Action Figures).
- **Sub-Categories**: Stores specific groups (e.g., Robots, Accessories) linked to a parent category.
- **Products**: Individual items assigned to a specific sub-category.

## 2. Relationships & ERD Strategy
- **One-to-Many Relationship**: Each `category` can have many `sub_categories`.
- **Singular Naming Convention**: Foreign keys follow the standard naming rule (`category_id`) for clarity and consistency.
- **Hierarchical Structure**: The design allows for easy navigation from a broad category down to specific products.

## 3. Schema Summary
| Entity | Relationship | Target Entity | Type |
| :--- | :--- | :--- | :--- |
| Category | Contains | Sub-Categories | One-to-Many |
| Sub-Category | Contains | Products | One-to-Many |

> **Pro Tip**: To support the "Browse by Brand/Character" feature shown in the wireframe, we could implement a **Many-to-Many** relationship between products and a generic `tags` table.