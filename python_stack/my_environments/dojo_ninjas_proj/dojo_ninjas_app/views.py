from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Home page — display all dojos and their ninjas
def index(request):
    dojos = Dojo.objects.all()
    return render(request, 'index.html', {'dojos': dojos})

# Page: form to add a new dojo
def new_dojo(request):
    return render(request, 'new_dojo.html')

# Page: form to add a new ninja
def new_ninja(request):
    dojos = Dojo.objects.all()
    return render(request, 'new_ninja.html', {'dojos': dojos})

# Process: create a new dojo
def create_dojo(request):
    Dojo.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state']
    )
    return redirect('/')

# Process: create a new ninja
def create_ninja(request):
    dojo = Dojo.objects.get(id=request.POST['dojo_id'])
    Ninja.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        dojo=dojo
    )
    return redirect('/')

# Process: delete a dojo (and all its ninjas via CASCADE)
def delete_dojo(request, id):
    Dojo.objects.get(id=id).delete()
    return redirect('/')