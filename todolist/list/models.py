from django.db import models


class Tasks(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True, default=None)
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    in_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
