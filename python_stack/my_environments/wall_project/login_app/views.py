from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    if 'user_id' in request.session: return redirect('/wall')
    return render(request, 'register.html')

def login_page(request):
    if 'user_id' in request.session: return redirect('/wall')
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.register_validator(request.POST)
        if errors:
            for k, v in errors.items(): messages.error(request, v, extra_tags='register')
            return redirect('/')
        
        # التشفير وحفظ البيانات
        hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            birthday=request.POST['birthday'],
            password=hash_pw
        )
        request.session['user_id'] = new_user.id
        return redirect('/wall') # التوجيه للحائط فور النجاح
    return redirect('/')

def login(request):
    if request.method == "POST":
        user_list = User.objects.filter(email=request.POST['email'])
        if user_list:
            logged_user = user_list[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect('/wall')
        
        messages.error(request, "Invalid email or password.", extra_tags='login')
        return redirect('/login_page')
    return redirect('/login_page')

def logout(request):
    request.session.flush() 
    # تصفير الجلسة بالكامل كما بالمتطلبات
    return redirect('/')