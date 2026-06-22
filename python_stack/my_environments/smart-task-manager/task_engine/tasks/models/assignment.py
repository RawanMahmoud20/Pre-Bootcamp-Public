from django.db import models
from django.utils import timezone
from django.conf import settings


class TaskAssignment(models.Model):
    task = models.ForeignKey(
        'tasks.Task',
        on_delete=models.CASCADE,
        related_name='assignments',
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='task_assignments',
    )
    assigned_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'task_assignments'
        unique_together = ('task', 'user')

    def __str__(self):
        return f'{self.user} → {self.task}'
