from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User, Book

# 1. Registration and Login Gateway
def index(render_request):
    if 'user_id' in render_request.session:
        return redirect('/books')
    return render(render_request, 'index.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/')
        
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=hashed_pw
        )
        request.session['user_id'] = new_user.id
        return redirect('/books')
    return redirect('/')

def login(request):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST['email']).first()
        if user and bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user_id'] = user.id
            return redirect('/books')
        messages.error(request, "Invalid Email or Password", extra_tags="login")
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

# 2. Books Dashboard (Main Page)
def books_dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'logged_user': User.objects.get(id=request.session['user_id']),
        'all_books': Book.objects.all()
    }
    return render(request, 'dashboard.html', context)

def create_book(request):
    if request.method == "POST":
        errors = Book.objects.book_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/books')
        
        user = User.objects.get(id=request.session['user_id'])
        new_book = Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc'],
            uploaded_by=user
        )
        # Auto feature: the uploader automatically likes their own book upon creation
        new_book.users_who_like.add(user)
    return redirect('/books')

# 3. Book Detail, Update, and Delete
def book_detail(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'logged_user': User.objects.get(id=request.session['user_id']),
        'book': Book.objects.get(id=book_id)
    }
    return render(request, 'book_detail.html', context)

def update_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.session['user_id'] == book.uploaded_by.id and request.method == "POST":
        errors = Book.objects.book_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/books/{book_id}')
        book.title = request.POST['title']
        book.desc = request.POST['desc']
        book.save()
    return redirect(f'/books/{book_id}')

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.session['user_id'] == book.uploaded_by.id:
        book.delete()
    return redirect('/books')

# 4. Like Features (Many-to-Many Actions)
def add_favorite(request, book_id):
    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=book_id)
    book.users_who_like.add(user)
    return redirect(request.META.get('HTTP_REFERER', '/books'))

def remove_favorite(request, book_id):
    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=book_id)
    book.users_who_like.remove(user)
    return redirect(request.META.get('HTTP_REFERER', '/books'))

# SENSEI BONUS: Display user profile and their favorite books
def user_profile(request, user_id):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'user_profile.html', context)