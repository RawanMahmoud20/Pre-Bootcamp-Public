from django.shortcuts import render, redirect
import random

def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
        request.session['attempts'] = 0
    
    return render(request, 'index.html')

def guess(request):
    user_guess = int(request.POST['guess'])
    target = request.session['number']
    request.session['attempts'] += 1
    request.session.modified = True
    attempts = request.session['attempts']

    if user_guess < target:
        result = 'low'
    elif user_guess > target:
        result = 'high'
    else:
        result = 'correct'

    # SENSEI: max 5 attempts
    if attempts >= 5 and result != 'correct':
        result = 'lose'

    return render(request, 'index.html', {
        'result': result,
        'guess': user_guess,
        'target': target,
        'attempts': attempts
    })

def reset(request):
    del request.session['number']
    del request.session['attempts']
    return redirect('/')