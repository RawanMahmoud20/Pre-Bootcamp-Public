from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User, Message, Comment

# 1. شاشات تسجيل الدخول والتسجيل
def signin_page(request):
    if 'user_id' in request.session:
        return redirect('/dashboard')
    return render(request, 'signin.html')

def register_page(request):
    if 'user_id' in request.session:
        return redirect('/dashboard')
    return render(request, 'register.html')

def logout(request):
    request.session.flush()
    return redirect('/signin')

# 2. معالجة البيانات الخلفية
def process_registration(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/register')
        
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        
        # أول مستخدم يسجل في الموقع نجعله الإدمن تلقائياً لتسهيل التجربة
        user_level = 'admin' if User.objects.count() == 0 else 'normal'
        
        user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=hashed_pw,
            user_level=user_level
        )
        request.session['user_id'] = user.id
        request.session['user_level'] = user.user_level
        return redirect('/dashboard')
    return redirect('/register')

def process_login(request):
    if request.method == "POST":
        user_list = User.objects.filter(email=request.POST['email'])
        if user_list:
            user = user_list[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                request.session['user_level'] = user.user_level
                return redirect('/dashboard')
        messages.error(request, "Invalid Email or Password")
    return redirect('/signin')

# 3. لوحات التحكم (Dashboards)
def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/signin')
    
    if request.session['user_level'] == 'admin':
        return redirect('/dashboard/admin')
        
    context = {
        'current_user': User.objects.get(id=request.session['user_id']),
        'all_users': User.objects.all()
    }
    return render(request, 'dashboard_normal.html', context)

def admin_dashboard(request):
    if 'user_id' not in request.session or request.session['user_level'] != 'admin':
        return redirect('/dashboard')
        
    context = {
        'current_user': User.objects.get(id=request.session['user_id']),
        'all_users': User.objects.all()
    }
    return render(request, 'dashboard_admin.html', context)

# 4. وظائف الإدمن (إضافة وحذف)
def add_user_page(request):
    if 'user_id' not in request.session or request.session['user_level'] != 'admin':
        return redirect('/dashboard')
    return render(request, 'add_user.html')

def process_add_user(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/users/new')
        
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=hashed_pw,
            user_level=request.POST['user_level']
        )
        return redirect('/dashboard')
    return redirect('/dashboard')

def delete_user(request, user_id):
    if 'user_id' not in request.session or request.session['user_level'] != 'admin':
        return redirect('/dashboard')
    User.objects.get(id=user_id).delete()
    return redirect('/dashboard')

# 5. عرض الملف الشخصي وجدار الرسائل (The Wall)
def show_user_profile(request, user_id):
    if 'user_id' not in request.session:
        return redirect('/signin')
        
    profile_user = User.objects.get(id=user_id)
    context = {
        'profile_user': profile_user,
        'current_user': User.objects.get(id=request.session['user_id']),
        # جلب الرسائل المكتوبة لهذا المستخدم مع تعليقاتها
        'wall_messages': Message.objects.filter(receiver=profile_user).order_by('-created_at')
    }
    return render(request, 'user_profile.html', context)

def post_message(request, receiver_id):
    if request.method == "POST" and 'user_id' in request.session:
        Message.objects.create(
            message_text=request.POST['message_text'],
            poster=User.objects.get(id=request.session['user_id']),
            receiver=User.objects.get(id=receiver_id)
        )
    return redirect(f'/users/show/{receiver_id}')

def post_comment(request, message_id):
    if request.method == "POST" and 'user_id' in request.session:
        msg = Message.objects.get(id=message_id)
        Comment.objects.create(
            comment_text=request.POST['comment_text'],
            poster=User.objects.get(id=request.session['user_id']),
            message=msg
        )
        return redirect(f'/users/show/{msg.receiver.id}')
    return redirect('/dashboard')

# 6. تعديلات الملف الشخصي
def edit_user_page(request, user_id):
    if 'user_id' not in request.session:
        return redirect('/signin')
    
    # منع المستخدم العادي من تعديل بيانات غيره
    if request.session['user_level'] != 'admin' and request.session['user_id'] != user_id:
        return redirect('/dashboard')
        
    context = {
        'target_user': User.objects.get(id=user_id),
        'current_user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'edit_user.html', context)

def process_edit_info(request, user_id):
    if request.method == "POST":
        user = User.objects.get(id=user_id)
        user.email = request.POST['email']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        if request.session['user_level'] == 'admin' and 'user_level' in request.POST:
            user.user_level = request.POST['user_level']
        user.save()
    return redirect('/dashboard')

def process_edit_password(request, user_id):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password_confirm']:
            user = User.objects.get(id=user_id)
            user.password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            user.save()
    return redirect('/dashboard')

def process_edit_description(request, user_id):
    if request.method == "POST":
        user = User.objects.get(id=user_id)
        user.description = request.POST['description']
        user.save()
    return redirect(f'/users/show/{user_id}')