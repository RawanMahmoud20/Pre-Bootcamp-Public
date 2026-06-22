from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=45)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='categories',
    )

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        unique_together = ('name', 'user')

    def __str__(self):
        return self.name