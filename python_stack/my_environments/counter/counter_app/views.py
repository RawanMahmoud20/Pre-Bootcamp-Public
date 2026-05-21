from django.shortcuts import render, redirect

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
        request.session['visits'] = 0
    
    request.session['counter'] += 1
    request.session['visits'] += 1
    request.session.modified = True
    
    return render(request, 'index.html', {
        'counter': request.session['counter'],
        'visits': request.session['visits']
    })

def destroy_session(request):
    del request.session['counter']
    del request.session['visits']
    return redirect('/')

def increment_by_two(request):  # NINJA BONUS
    request.session['counter'] += 2
    request.session.modified = True
    return redirect('/')