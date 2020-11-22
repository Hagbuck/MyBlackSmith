from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Project(models.Model):
    name = models.CharField(max_length = 256)
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    description = models.CharField(max_length = 2048)
    creation_date = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name
