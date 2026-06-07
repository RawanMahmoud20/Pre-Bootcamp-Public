from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    
    
class Book(models.Model):
    title   = models.CharField(max_length=255)
    desc    = models.CharField(max_length=45)
    authors = models.ManyToManyField(Author, related_name='books')