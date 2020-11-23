from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ['user', 'creation_date']

admin.site.register(Project, ProjectAdmin)
