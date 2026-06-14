from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User, Book, Review

# 1. Display the registration page (home)
def index(request):
    if 'user_id' in request.session:
        return redirect('/books')
    return render(request, 'register.html')

# Additional function to display the standalone login page
def login_page(request):
    if 'user_id' in request.session:
        return redirect('/books')
    return render(request, 'login.html')

# 2. Handle new user registration
def register(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags='register')
            return redirect('/')
        
        # Hash the password and save the new fields
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            birthday=request.POST['birthday'],
            password=hashed_pw
        )
        request.session['user_id'] = user.id
        messages.success(request, "Successfully registered!", extra_tags='status')
        return redirect('/books')
    return redirect('/')

# 3. Handle login
def login(request):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST['email'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                messages.success(request, "Successfully logged in!", extra_tags='status')
                return redirect('/books')
        
        messages.error(request, "Invalid Email or Password.", extra_tags='login')
        return redirect('/login_page')
    return redirect('/login_page')

# 4. Logout
def logout(request):
    request.session.flush()
    return redirect('/login_page')

# 5. Main dashboard after login
def books(request):
    if 'user_id' not in request.session:
        return redirect('/login_page')
    
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'recent_reviews': Review.objects.all().order_by('-created_at')[:3],
        'all_books': Book.objects.all()
    }
    return render(request, 'success.html', context)

# 6. Add new book form page
def add_book_page(request):
    if 'user_id' not in request.session:
        return redirect('/login_page')
    
    context = {
        'authors': Book.objects.values_list('author', flat=True).distinct()
    }
    return render(request, 'add_book.html', context)

# 7. Handle creating a book and its first review
def create_book_and_review(request):
    if request.method == "POST":
        if request.POST.get('custom_author'):
            author = request.POST['custom_author']
        else:
            author = request.POST['selected_author']
            
        book = Book.objects.create(title=request.POST['title'], author=author)
        user = User.objects.get(id=request.session['user_id'])
        Review.objects.create(
            review=request.POST['review'], 
            rating=int(request.POST['rating']), 
            user=user, 
            book=book
        )
        return redirect(f'/books/{book.id}')
    return redirect('/books')

# 8. Show specific book details and its reviews
def show_book(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/login_page')
        
    context = {
        'book': Book.objects.get(id=book_id),
        'current_user_id': request.session['user_id']
    }
    return render(request, 'book_detail.html', context)

# 9. Add an additional review to an existing book
def create_review(request, book_id):
    if request.method == "POST":
        user = User.objects.get(id=request.session['user_id'])
        book = Book.objects.get(id=book_id)
        Review.objects.create(
            review=request.POST['review'], 
            rating=int(request.POST['rating']), 
            user=user, 
            book=book
        )
    return redirect(f'/books/{book_id}')

# 10. Delete a review
def delete_review(request, review_id):
    if 'user_id' not in request.session:
        return redirect('/login_page')
        
    review = Review.objects.get(id=review_id)
    if review.user.id == request.session['user_id']:
        book_id = review.book.id
        review.delete()
        return redirect(f'/books/{book_id}')
    return redirect('/books')

# 11. User profile page and statistics
def show_user(request, user_id):
    if 'user_id' not in request.session:
        return redirect('/login_page')
        
    user = User.objects.get(id=user_id)
    context = {
        'user': user,
        'total_reviews': user.reviews_left.count(),
        'reviewed_books': Book.objects.filter(reviews__user=user).distinct()
    }
    return render(request, 'user_profile.html', context)