# User Dashboard ERD Implementation

## Project Description
This project focuses on designing a scalable database schema for a User Dashboard system. It goes beyond simple data storage to capture user interactions and administrative levels.

## Database Design Strategy
Based on the wireframe requirements:
- **Normalization**: Data is split into multiple tables (`users`, `roles`, `messages`) to ensure integrity.
- **Scalability**: The design supports adding more features like logs or permissions without breaking the existing structure.
- **Security**: Includes fields for hashed passwords and user access levels.

## Schema Components
1. **Users**: The core entity storing identity and credentials.
2. **User Levels**: A numeric representation of permissions (as hinted in common dashboard functionalities).
3. **Interactions**: Tables to record actions (like messages or updates) performed by the user.

## Execution
To set up this database, run the `user_dashboard.sql` file in your MySQL environment.