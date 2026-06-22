from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth_view, name='auth'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('tasks/', views.tasks_view, name='tasks'),
    path('about/', views.about_view, name='about'),

    # AJAX endpoints
    path('api/tasks/', views.task_list_json, name='task_list_json'),
    path('api/tasks/create/', views.task_create, name='task_create'),
    path('api/tasks/<int:pk>/status/', views.task_update_status, name='task_update_status'),
    path('api/tasks/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('api/tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
    # Category endpoints
    path('api/categories/', views.category_list_json, name='category_list_json'),
    path('api/categories/create/', views.category_create, name='category_create'),
    path('api/categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
]
