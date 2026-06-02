from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    dojos = Dojo.objects.all()
    return render(request, 'index.html', {'dojos': dojos})
def create_dojo(request):
    Dojo.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state']
    )
    return redirect('/')
def create_ninja(request):
    dojo = Dojo.objects.get(id=request.POST['dojo_id'])
    Ninja.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        dojo=dojo
    )
    return redirect('/')

# NINJA BONUS
def delete_dojo(request, id):
    Dojo.objects.get(id=id).delete()
    return redirect('/')
