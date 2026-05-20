# Django Time Display Assignment

A simple, structured Django web application designed to demonstrate the fundamentals of views, template rendering, routing, and static file architecture by displaying the live localized date and time.

## Project Architecture
```text
time_display_project/
│
├── time_display/           # Core Application App
│   ├── static/             # Static Assets Directory
│   │   └── css/
│   │       └── style.css   # Custom Stylesheet
│   ├── templates/          # HTML Templates
│   │   └── index.html      # Main Presentation Layer
│   ├── urls.py             # App Routing
│   └── views.py            # App Controller / Logic
│
└── project_settings/       # Project Configuration Window
    └── urls.py             # Global Routing