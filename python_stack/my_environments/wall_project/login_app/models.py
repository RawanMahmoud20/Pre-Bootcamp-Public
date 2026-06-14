from django.db import models
import re
from datetime import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        # التحقق من الأسماء
        if len(postData['first_name']) < 2 or not postData['first_name'].isalpha():
            errors['first_name'] = "First name must be at least 2 characters and contain letters only."
        if len(postData['last_name']) < 2 or not postData['last_name'].isalpha():
            errors['last_name'] = "Last name must be at least 2 characters and contain letters only."
        
        # التحقق من البريد الإلكتروني وتفرده (Ninja Bonus)
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address format."
        elif User.objects.filter(email=postData['email']).exists():
            errors['email'] = "This email is already registered."
        
        # التحقق من تاريخ الميلاد والعمر (Sensei Bonus - COPPA)
        if postData['birthday']:
            b_date = datetime.strptime(postData['birthday'], '%Y-%m-%d')
            if b_date >= datetime.now():
                errors['birthday'] = "Birthday must be in the past."
            elif (datetime.now() - b_date).days < 4748: # 13 سنة بالليالي والأيام
                errors['birthday'] = "You must be at least 13 years old to register."
        else:
            errors['birthday'] = "Birthday field is required."

        # التحقق من كلمة المرور
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters long."
        elif postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = "Passwords do not match."
            
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()