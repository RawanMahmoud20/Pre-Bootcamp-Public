from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData.get('name', '').strip()) <= 5:
            errors['name'] = "Course name must be more than 5 characters long."
        if len(postData.get('description', '').strip()) <= 15:
            errors['description'] = "Description must be more than 15 characters long."
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = CourseManager()

class Description(models.Model):
    # تحقيق شرط الـ One-to-One Relationship
    course = models.OneToOneField(Course, on_delete=models.CASCADE, primary_key=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)