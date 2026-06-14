# Favorite Books Application (Django)

An advanced Full-Stack Web Application built using Python and the Django framework. This project demonstrates database design principles, focusing on **One-to-Many** and **Many-to-Many** relationships by allowing users to register, upload their favorite books, view submissions from other users, and add books to their personal "Favorites" list.

## 🚀 Objectives & Features

### 1. Authentication & Security
* **User Registration:** Complete input validations for First Name, Last Name, Email formatting (Regex), Email uniqueness, and Password strength.
* **User Login:** Secure password verification against database records.
* **Password Hashing:** Implemented secure password encryption using the `bcrypt` library.
* **Session Management:** Keeps users securely logged in and protects restricted dashboard routes.

### 2. Book Management (One-to-Many Relationship)
* Registered users can upload new books with validated fields (Title and Description).
* Tracks which specific user uploaded each book instance (`uploaded_by` ForeignKey).
* **Access Control:** Only the user who originally uploaded a book can edit its details or permanently delete it from the system.

### 3. Favoriting System (Many-to-Many Relationship)
* Users can mark books as their favorites, linking multiple users to multiple books (`users_who_like` ManyToManyField).
* Books uploaded by a user are automatically favorited by them upon creation.
* Users can smoothly "Favorite" or "Unfavorite" books dynamically across the platform.

### 4. Advanced Bonuses (Sensei & Ninja Bonus)
* **Ninja Bonus:** Dynamic conditional rendering on UI elements; the "Add to Favorites" link hides or updates to a "this is one of your favorites" status message if already favorited.
* **Sensei Bonus:** Dedicated User Profile view (`/users/<id>`) showcasing specialized account stats alongside a clean list of all books favorited by that particular user.

---

## 🛠️ Tech Stack
* **Backend Framework:** Django 
* **Programming Language:** Python 3
* **Database:** SQLite3 (Default relational storage mapped via Django ORM)
* **Security:** Bcrypt (Password Hashing)

---

## ⚙️ Installation & Setup Guide

Follow these sequential steps to spin up the application on your local machine:

### 1. Clone or Extract the Project
Navigate to your working directory containing the project:
```bash
cd favorite_books_project