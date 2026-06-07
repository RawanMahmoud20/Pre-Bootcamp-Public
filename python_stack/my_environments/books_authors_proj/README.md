# Books/Authors with Templates

## Project Description
A full-stack Django app that implements a Many-to-Many relationship between Books and Authors with a Bootstrap UI.

---

## File Structure
books_authors_proj/
├── books_authors_proj/
│   ├── settings.py
│   └── urls.py
└── books_authors_app/
├── models.py
├── views.py
├── urls.py
└── templates/
├── all_books.html
├── show_book.html
├── all_authors.html
└── show_author.html
---

## Pages & URLs

| URL | Description |
|-----|-------------|
| `/books/` | Display all books + add a new book |
| `/books/<id>/` | Book details + add an author to it |
| `/authors/` | Display all authors + add a new author |
| `/authors/<id>/` | Author details + add a book to them |

---

## How to Run

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Then open your browser at:
- http://127.0.0.1:8000/books/
- http://127.0.0.1:8000/authors/

---

## Bonus
The dropdown on each detail page only shows items not yet associated with the current book or author. This was implemented using `.exclude()` in the views.