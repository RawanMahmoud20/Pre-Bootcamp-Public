from django.shortcuts import render , redirect

# Create your views here.

def index(request):
    # display the form
    return render(request, 'index.html')

def result(request):
    if request.method == "POST":
        print(request.POST)
        
        context = {
            "name": request.POST.get('name'),
            "location": request.POST.get('location'),
            "language": request.POST.get('language'),
            "gender": request.POST.get('gender'), # Ninja Bonus (Radio)
            "interests": request.POST.getlist('interests'), # Sensei Bonus (Checkboxes)
            "comment": request.POST.get('comment'),
        }
        return render(request, 'result.html', context)
    return redirect('/')