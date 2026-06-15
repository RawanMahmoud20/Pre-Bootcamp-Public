from django.http import HttpResponse

def register(request):
    return HttpResponse("placeholder for users to create a new user record.")

def login_view(request):
    return HttpResponse("placeholder for users to log in.")

def index(request):
    return HttpResponse("placeholder to display all the list of users later.")

def info(request, game_id):
    if 'user_id' not in request.session:
        return redirect('/')
    game = Game.objects.get(id=game_id)
    context = {
        'game': game,
        'players_roles': PlayerRole.objects.filter(game=game),
        'current_user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'game_info.html', context)

def edit(request, game_id):
    if 'user_id' not in request.session:
        return redirect('/')
    game = Game.objects.get(id=game_id)
    if game.creator.id != request.session['user_id']:
        return redirect('/dashboard')
        
    if request.method == "POST":
        errors = Game.objects.game_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/games/{game_id}/edit')
        
        game.title = request.POST['title']
        game.genre = request.POST['genre']
        game.release_date = request.POST['release_date']
        game.description = request.POST['description']
        game.save()
        return redirect('/dashboard')
        
    return render(request, 'edit_game.html', {'game': game})

def delete(request, game_id):
    if 'user_id' not in request.session:
        return redirect('/')
    game = Game.objects.get(id=game_id)
    if game.creator.id == request.session['user_id']:
        game.delete()
    return redirect('/dashboard')

def join(request, game_id):
    
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == "POST":
        user = User.objects.get(id=request.session['user_id'])
        game = Game.objects.get(id=game_id)
        PlayerRole.objects.update_or_create(
            user=user, game=game,
            defaults={'role': request.POST['role']}
        )
    return redirect(f'/games/{game_id}')

# 11. صفحة ملف المستخدم الشخصي (صورة الـ Avatar)
def user_profile(request, user_id):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request, 'profile.html', {'profile_user': User.objects.get(id=user_id)})