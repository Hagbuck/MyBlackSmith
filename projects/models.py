from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Project(models.Model):
    name = models.CharField(max_length = 256)
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, editable=False)
    description = models.CharField(max_length = 2048)
    creation_date = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    name = models.CharField(max_length = 256)
    text = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now, editable=False)

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete = models.CASCADE)
    text = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now, editable=False)

class Label(models.Model):
    name = models.CharField(max_length = 64)
    creation_date = models.DateTimeField(default=timezone.now, editable=False)