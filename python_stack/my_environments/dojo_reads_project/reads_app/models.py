from django.db import models
import re
from datetime import datetime

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters."
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters."
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid email address."
        if User.objects.filter(email=postData['email']).exists():
            errors["email_exists"] = "Email is already registered."
        if not postData['birthday']:
            errors["birthday"] = "Birthday is required."
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters."
        if postData['password'] != postData['confirm_password']:
            errors["confirm_password"] = "Passwords do not match."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birthday = models.DateField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name="reviews_left", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name="reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)