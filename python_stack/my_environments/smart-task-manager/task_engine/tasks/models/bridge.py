from django.db import models


class TaskCategory(models.Model):
    task = models.ForeignKey(
        'tasks.Task',
        on_delete=models.CASCADE,
        related_name='task_categories',
    )
    category = models.ForeignKey(
        'tasks.Category',
        on_delete=models.CASCADE,
        related_name='task_categories',
    )

    class Meta:
        db_table = 'task_categories'
        unique_together = ('task', 'category')

    def __str__(self):
        return f'{self.task} / {self.category}'
