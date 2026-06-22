from django.db import models
from django.conf import settings


class Task(models.Model):
    STATUS_PENDING = 'Pending'
    STATUS_IN_PROGRESS = 'In Progress'
    STATUS_COMPLETED = 'Completed'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_IN_PROGRESS, 'In Progress'),
        (STATUS_COMPLETED, 'Completed'),
    ]

    title = models.CharField(max_length=45)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=45, choices=STATUS_CHOICES, default=STATUS_PENDING)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owned_tasks',
    )

    class Meta:
        db_table = 'tasks'
        ordering = ['due_date']

    def __str__(self):
        return self.title
