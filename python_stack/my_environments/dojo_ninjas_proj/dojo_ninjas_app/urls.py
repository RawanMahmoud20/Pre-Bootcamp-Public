from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_dojo', views.new_dojo),
    path('new_ninja', views.new_ninja),
    path('create_dojo', views.create_dojo),
    path('create_ninja', views.create_ninja),
    path('delete_dojo/<int:id>', views.delete_dojo),
]