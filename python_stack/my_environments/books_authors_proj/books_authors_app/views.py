from django.shortcuts import render, redirect
from .models import Book, Author

def all_books(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc']
        )
        return redirect('/books/')
    books = Book.objects.all()
    return render(request, 'all_books.html', {'books': books})

def show_book(request, id):
    book = Book.objects.get(id=id)
    authors_not_in_book = Author.objects.exclude(id__in=book.authors.all())
    return render(request, 'show_book.html', {
        'book': book,
        'other_authors': authors_not_in_book
    })

def add_author_to_book(request, id):
    if request.method == "POST":
        book = Book.objects.get(id=id)
        author = Author.objects.get(id=request.POST['author_id'])
        book.authors.add(author)
    return redirect(f'/books/{id}/')

def all_authors(request):
    if request.method == "POST":
        Author.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            notes=request.POST['notes']
        )
        return redirect('/authors/')
    authors = Author.objects.all()
    return render(request, 'all_authors.html', {'authors': authors})

def show_author(request, id):
    author = Author.objects.get(id=id)
    books_not_with_author = Book.objects.exclude(id__in=author.books.all())
    return render(request, 'show_author.html', {
        'author': author,
        'other_books': books_not_with_author
    })

def add_book_to_author(request, id):
    if request.method == "POST":
        author = Author.objects.get(id=id)
        book = Book.objects.get(id=request.POST['book_id'])
        author.books.add(book)
    return redirect(f'/authors/{id}/')