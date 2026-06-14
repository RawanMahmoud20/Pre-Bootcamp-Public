from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),                  # صفحة التسجيل الأساسية
    path('login_page', views.login_page),   # صفحة اللوجين المنفصلة (الجديدة)
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
]