from django.db import models
import re
from datetime import date , datetime

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if len(postData.get('first_name', '')) < 2:
            errors["first_name"] = "First name should be at least 2 characters."
        if len(postData.get('last_name', '')) < 2:
            errors["last_name"] = "Last name should be at least 2 characters."
        if not EMAIL_REGEX.match(postData.get('email', '')):
            errors["email"] = "Invalid email address."
        if User.objects.filter(email=postData.get('email', '')).exists():
            errors["email_exists"] = "Email is already registered."
        if not postData.get('birth_date'):
            errors["birth_date"] = "Birthday is required."
        if len(postData.get('password', '')) < 8:
            errors["password"] = "Password should be at least 8 characters."
        if postData.get('password') != postData.get('confirm_password'):
            errors["confirm_password"] = "Passwords do not match."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birth_date = models.DateField()
    password = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True) # تفعيل رفع الصور للاختبار
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class GameManager(models.Manager):
    def game_validator(self, postData):
        errors = {}
        if len(postData.get('title', '')) < 2:
            errors['title'] = "The Name of Game should be at least 2 characters"
        if not postData.get('genre'):
            errors['genre'] = "Genre is required."
        if len(postData.get('description', '')) < 10:   
            errors['description'] = "The Description should be at least 10 characters"
        
        release_date_str = postData.get('release_date')
        if release_date_str:
            if date.fromisoformat(release_date_str) > date.today():
                errors['release_date'] = "Release date must be in the past"
        else:
            errors['release_date'] = "Release is required."
        return errors     

class Game(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games')
    players = models.ManyToManyField(User, related_name='game_player', through='PlayerRole')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = GameManager()
    
    def __str__(self):
        return self.title
    
class PlayerRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    role = models.CharField(max_length=255) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)