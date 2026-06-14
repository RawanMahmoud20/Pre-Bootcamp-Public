from django.db import models
import re
from datetime import datetime, timedelta # You'll need this to calculate age and dates

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        
        # 1. Validate first name
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters long."
        elif not postData['first_name'].isalpha():
            errors['first_name'] = "First name must contain letters only."
            
        # 2. Validate last name
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters long."
        elif not postData['last_name'].isalpha():
            errors['last_name'] = "Last name must contain letters only."
            
        # 3. Validate email
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email format."
        else:
            if User.objects.filter(email=postData['email']).exists():
                errors['email'] = "This email is already registered."
                
        # 4. [NINJA & SENSEI BONUS] Validate birthday
        if not postData['birthday']:
            errors['birthday'] = "Birthday is required."
        else:
            # Convert the string from the front-end into a date object
            birthday = datetime.strptime(postData['birthday'], '%Y-%m-%d')
            
            # Make sure the date is in the past
            if birthday >= datetime.now():
                errors['birthday'] = "Birthday must be in the past."
            
            # Make sure the user is at least 13 years old (COPPA compliant)
            # 13 years equals approximately 4748 days (accounting for leap years)
            elif (datetime.now() - birthday).days < 4748:
                errors['birthday'] = "You must be at least 13 years old to register."

        # 5. Validate password
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters long."
        elif postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = "Password and confirmation do not match."
            
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    # Added birthday field
    birthday = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()