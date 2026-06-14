from django.urls import path
from . import views

urlpatterns = [
    # Login and account gateway pages
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    
    # Book pages and operations
    path('books', views.books_dashboard),
    path('books/create', views.create_book),
    path('books/<int:book_id>', views.book_detail),
    path('books/<int:book_id>/update', views.update_book),
    path('books/<int:book_id>/delete', views.delete_book),
    
    # Like and unlike operations
    path('books/<int:book_id>/favorite', views.add_favorite),
    path('books/<int:book_id>/unfavorite', views.remove_favorite),
    
    # SENSEI BONUS: User profile page showing their favorite books
    path('users/<int:user_id>', views.user_profile),
]