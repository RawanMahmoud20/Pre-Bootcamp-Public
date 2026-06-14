from django.urls import path
from . import views
# (Login & Registration)

urlpatterns = [
path('',views.index),
path('register', views.register),
path('login', views.login),
path('logout', views.logout),
# page of book , review 
path('books', views.books),
path('books/add', views.add_book_page),
path('books/create', views.create_book_and_review),
path('books/<int:book_id>', views.show_book),
path('books/<int:book_id>/review', views.create_review),

# delete review and user profile
path('reviews/<int:review_id>/delete', views.delete_review),
path('users/<int:user_id>', views.show_user),
]