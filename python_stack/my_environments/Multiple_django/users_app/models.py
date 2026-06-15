from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if len(postData.get('first_name', '')) < 2:
            errors['first_name'] = "First name should be at least 2 characters"
        if len(postData.get('last_name', '')) < 2:
            errors['last_name'] = "Last name should be at least 2 characters"
        if not EMAIL_REGEX.match(postData.get('email', '')):
            errors['email'] = "Invalid email address"
        if User.objects.filter(email=postData.get('email', '')).exists():
            errors['email_exists'] = "Email is already registered"
        if len(postData.get('password', '')) < 8:
            errors['password'] = "Password should be at least 8 characters"
        if postData.get('password') != postData.get('password_confirm'):
            errors['password_confirm'] = "Passwords do not match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    # user_level: 'admin' للمسؤول و 'normal' للمستخدم العادي كما بالوايرفريم
    user_level = models.CharField(max_length=20, default='normal')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Message(models.Model):
    message_text = models.TextField()
    # المستخدم الذي كتب الرسالة
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages_posted")
    # المستخدم الذي كُتبت الرسالة على جدار ملفه الشخصي
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages_received")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment_text = models.TextField()
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)