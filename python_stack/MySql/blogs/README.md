# Assignment: Blogs System Implementation

## Project Overview
This project focuses on building a robust database schema for a blog management platform. It allows users to register, create and manage blogs, and collaborate with other users as co-administrators.

## Core Features
- **User Authentication**: Secure storage for user credentials.
- **Hierarchical Content**: Blogs contain multiple posts, and posts contain files and comments.
- **Administrative Rights**: Support for shared administrative access to blogs through a many-to-many relationship.
- **User Analytics**: Tracking system for page visits, duration, and user IP addresses.

## Technical Implementation
- **Schema**: Relational Database Design using MySQL.
- **Normalization**: Tables are normalized to reduce redundancy, utilizing foreign keys and bridge tables (e.g., `blog_admins`).
- **Data Integrity**: Enforced using PRIMARY KEY and FOREIGN KEY constraints with CASCADE deletion rules.

## How to use
Execute the provided SQL script in your MySQL Workbench or preferred database tool to generate the platform structure.