from django.db import models
from django.utils import timezone
from colorfield.fields import ColorField
from django.contrib.auth import get_user_model

from projects.models import Project

class Label(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, editable = False)
    project = models.ForeignKey(Project, on_delete = models.CASCADE, blank = True, null = True)
    name = models.CharField(max_length = 64)
    color = ColorField(default='#FFFFFF')
    creation_date = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name if not self.project else "{}@{}".format(self.name, self.project)