from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.all_books, name='all_books'),
    path('books/<int:id>/', views.show_book, name='show_book'),
    path('authors/', views.all_authors, name='all_authors'),
    path('authors/<int:id>/', views.show_author, name='show_author'),
    path('books/<int:id>/add_author/', views.add_author_to_book, name='add_author_to_book'),
    path('authors/<int:id>/add_book/', views.add_book_to_author, name='add_book_to_author'),
]