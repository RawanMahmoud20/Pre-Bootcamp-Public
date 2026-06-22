from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
