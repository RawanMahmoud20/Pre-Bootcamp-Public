from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
# Create your views here.
def index(request):
    context={
   "time": strftime("%b %d, %Y %I:%M %p", gmtime())
  }
    return render(request , 'index.html' , context)
