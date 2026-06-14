from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    # If the user is already logged in, redirect to the success page
    if 'user_id' in request.session:
        return redirect('/success')
    return render(request, 'register.html')

# --- New added function to display a separate login page ---
def login_page(request):
    if 'user_id' in request.session:
        return redirect('/success')
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        # Run validations
        errors = User.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags='register')
            return redirect('/')
        else:
            # Hash the password using bcrypt
            hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            
            # [Optional] If you used the Birthday Bonus, add the field here:
            new_user = User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                birthday=request.POST.get('birthday'), # Safely fetch the date field
                password=hash_pw
            )
            # Save the user in the Session and redirect
            request.session['user_id'] = new_user.id
            messages.success(request, "Registration successful!", extra_tags='status')
            return redirect('/success')
    return redirect('/')

def login(request):
    if request.method == "POST":
        user_list = User.objects.filter(email=request.POST['email'])
        if user_list:
            logged_user = user_list[0]
            # Verify the hashed password
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                messages.success(request, "Login successful!", extra_tags='status')
                return redirect('/success')
        
        # If login fails, send error and redirect back to login page (not home)
        messages.error(request, "Invalid email or password.", extra_tags='login')
        return redirect('/login_page')
        
    return redirect('/login_page')

def success(request):
    # Route protection: prevent access for non-logged-in users
    if 'user_id' not in request.session:
        return redirect('/')
    
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'success.html', context)

def logout(request):
    # Clear the session and redirect to the registration page
    request.session.flush()
    return redirect('/')