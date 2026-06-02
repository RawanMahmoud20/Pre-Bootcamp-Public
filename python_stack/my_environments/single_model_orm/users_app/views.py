from django.shortcuts import render, redirect
from .models import User

#display all user
def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})

# add new user
def create(request):
    User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email_address=request.POST['email_address'],
        age=request.POST['age']
    )
    return redirect('/users')