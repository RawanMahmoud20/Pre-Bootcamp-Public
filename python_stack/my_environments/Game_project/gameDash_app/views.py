from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from datetime import date, datetime

from .models import User, Game, PlayerRole

# 1. Display the registration page (home)
def index(request):
    if 'user_id' in request.session:
        return redirect('/dashboard')
    return render(request, 'register.html')

# Additional function to display the standalone login page
def login_page(request):
    if 'user_id' in request.session:
        return redirect('/dashboard')  # تم تصحيح التوجيه إلى الداشبورد بدلاً من صفحة الكتب القديمة
    return render(request, 'login.html')

# 2. Handle new user registration
def register(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags='register')
            return redirect('/')
        
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            birth_date=request.POST['birth_date'],
            password=hashed_pw,
            avatar=request.FILES.get('avatar')
        )
        request.session['user_id'] = user.id
        return redirect('/dashboard')
    return redirect('/')

# 3. Handle login
def login(request):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST['email'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect('/dashboard')
        
        messages.error(request, "Invalid Email or Password.", extra_tags='login')
        return redirect('/')
    return redirect('/')

# 4. Logout
def logout(request):
    request.session.flush()
    return redirect('/')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'current_user': User.objects.get(id=request.session['user_id']),
        'all_games': Game.objects.all().order_by('title')
    }
    return render(request, 'dashboard.html', context)

def create_game(request):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == "POST":
        errors = Game.objects.game_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/dashboard')    
        
        user = User.objects.get(id=request.session['user_id'])
        Game.objects.create(
            title=request.POST['title'],
            genre=request.POST['genre'],
            release_date=request.POST['release_date'],
            description=request.POST['description'],
            creator=user
        )
    return redirect('/dashboard') 

def game_info(request, game_id):
    if 'user_id' not in request.session:
        return redirect('/')
    game = Game.objects.get(id=game_id)
    context = {
        'game': game,
        'players_roles': PlayerRole.objects.filter(game=game), # تم تعديل الاسم ليتطابق تماماً مع حلقة التكرار في الـ HTML
        'current_user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'game_info.html', context)
    
def edit_game(request, game_id):
    if 'user_id' not in request.session:
        return redirect('/')
    game = Game.objects.get(id=game_id)
    if game.creator.id != request.session['user_id']:
        return redirect('/dashboard')
    
    if request.method == "POST":
        errors = Game.objects.game_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/games/{game_id}/edit') 

        
        game.title = request.POST['title']
        game.genre = request.POST['genre']
        
        release_date_str = request.POST.get('release_date')
        if release_date_str:
            game.release_date = release_date_str
        else:
            game.release_date = None      
                  
        game.description = request.POST['description']
        game.save()
        return redirect('/dashboard')
    return render(request, 'edit_game.html', {'game': game})

def delete_game(request, game_id):
    if 'user_id' not in request.session:
        return redirect('/')
    
    game = Game.objects.get(id=game_id)
    
    if game.creator.id == request.session['user_id']:
        game.delete()
    return redirect('/dashboard')
    
def join_game(request, game_id):
    if 'user_id' not in request.session:
        return redirect('/')
    
    if request.method == "POST":
        user = User.objects.get(id=request.session['user_id'])
        game = Game.objects.get(id=game_id)
       
        PlayerRole.objects.update_or_create(
            user=user, game=game,
            defaults={'role': request.POST['role']} 
        )      
    return redirect(f'/games/{game_id}')

def user_profile(request, user_id):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request, 'profile.html', {'profile_user': User.objects.get(id=user_id)})