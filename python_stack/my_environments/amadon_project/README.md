# Amadon E-Commerce Store

A secure, mini e-commerce application built with Python and Django. This project demonstrates critical web development best practices regarding form handling, request routing, and backend data validation.

---

## 🎯 Objectives & Key Concepts

This project was built to address two common security and architectural flaws found in poorly designed e-commerce platforms:

1. **Post/Redirect/Get (PRG) Pattern:** Avoids rendering an HTML page directly in response to an HTTP `POST` request. This prevents the user from accidentally resubmitting payment forms or being double-charged when reloading/refreshing the checkout page.
2. **Backend Price Validation:** Never trust user input or hidden HTML form values (like `<input type="hidden" name="price" ...>`). Malicious users can easily alter these values using browser DevTools (Inspect Element). Instead, the form only passes a `product_id`, and the server securely fetches the authentic price from the database.

---

## 🚀 Features

- Full list of available products styled cleanly with **Bootstrap**.
- Interactive purchase form where users choose quantities.
- Secure processing of orders in the backend.
- Persistent session and database tracking to display:
  - Current order total cost.
  - Cumulative total of items purchased across all historic orders.
  - Cumulative total amount spent across all historic orders.

---

## 🛠️ Project Structure

```text
amadon_project/
│
├── amadon/                  # Main application folder
│   ├── templates/
│   │   └── amadon/
│   │       ├── index.html   # Product listing page
│   │       └── checkout.html# Thank you / receipt page
│   ├── models.py            # Database tables (Product, Order)
│   ├── urls.py              # Application-specific routing
│   └── views.py             # App logic (Form handling, sessions, db aggregation)
│
├── amadon_project/          # Project configuration folder
│   ├── settings.py
│   └── urls.py
│
└── manage.py