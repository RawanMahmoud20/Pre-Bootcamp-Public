from django.db import models
from datetime import datetime


class ShowManager(models.Manager):
    def basic_validator(self, postData, show_id=None):
        errors = {}
        title = postData.get('title', '').strip()
        if len(title) < 2:
            errors['title'] = "Title should be at least 2 characters."
        else:
            # التحقق من أن الاسم فريد (مع استثناء المسلسل نفسه عند التعديل)
            existing_shows = Show.objects.filter(title=title)
            if show_id:
                existing_shows = existing_shows.exclude(id=show_id)
            if existing_shows.exists():
                errors['title'] = "A TV show with this title already exists."     
            # 2. التحقق من الشبكة
        if len(postData.get('network', '').strip()) < 3:
            errors['network'] = "Network should be at least 3 characters."
            
        # 3. التحقق من التاريخ (يجب أن يكون في الماضي)
        release_date_str = postData.get('release_date', '')
        if not release_date_str:
            errors['release_date'] = "Release date is required."
        else:
            release_date = datetime.strptime(release_date_str, '%Y-%m-%d').date()
            if release_date >= datetime.now().date():
                errors['release_date'] = "Release Date should be in the past."

        # 4. التحقق من الوصف (اختياري، لكن إذا وجد لا يقل عن 10)
        description = postData.get('description', '').strip()
        if description and len(description) < 10:
            errors['description'] = "Description is optional, but if present must be at least 10 characters."
            
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # ربط المانجر الجديد بالـ Model
    objects = ShowManager()  
