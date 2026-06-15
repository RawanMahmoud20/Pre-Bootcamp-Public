from django.urls import path
from . import views
# (Login & Registration)

urlpatterns = [
path('',views.index),
path('register', views.register),
path('login', views.login),
path('logout', views.logout),
path('dashboard', views.dashboard),
path('games/new', views.create_game),
path('games/<int:game_id>', views.game_info),
path('games/<int:game_id>/edit', views.edit_game),
path('games/<int:game_id>/delete', views.delete_game),
path('games/<int:game_id>/join', views.join_game),

path('profile/<int:user_id>', views.user_profile, name='user_profile'),
]