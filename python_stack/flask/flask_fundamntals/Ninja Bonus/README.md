# Flask Playground Assignment

This project is a Flask application designed to dynamically render HTML templates with varying numbers of boxes and colors based on the URL path. It implements a single HTML template and uses a custom CSS file.

## Project Structure

```text
playground/
│
├── server.py             # Main Flask application
├── static/
│   └── style.css         # External stylesheet for styling boxes
└── templates/
    └── index.html        # Jinja2 HTML template