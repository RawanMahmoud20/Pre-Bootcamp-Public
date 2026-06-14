Here is the translated version:

🔐 Login and Registration System (Django)
A full-featured web application for managing Registration and Login operations, built with the Django framework and styled with a clean and elegant Bootstrap 5 design.
🚀 Features

Fully Separated Pages: Registration and Login pages are completely separated for better user experience.
Secure Password Hashing: Passwords are protected and hashed in the database using the bcrypt library.
Strict Validation System:

First and last name (at least 2 characters, letters only).
Email (valid format, unique in the database Ninja Bonus).
Birthday (must be in the past, user must be at least 13 years old Sensei Bonus).
Password (at least 8 characters and must match the confirmation).


Flash Messages: Instant and accurate error/success notifications for each operation.
Route Protection: Prevents access to the success page (/success) without an active session.


🛠️ Tech Stack

Backend: Python 3.13+ / Django 5.x
Frontend: HTML5 / CSS3 / Bootstrap 5 (lightweight and clean styling)
Database: SQLite (Django's default)