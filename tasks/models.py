from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from projects.models import Project

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete = models.CASCADE, blank = True, null = True)
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, editable=False)
    name = models.CharField(max_length = 256)
    text = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete = models.CASCADE, editable=False)
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, editable=False)
    text = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.text[:30]