from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('destroy_session', views.destroy_session, name='destroy'),
    path('increment_by_two', views.increment_by_two, name='plus2'),  # NINJA
]