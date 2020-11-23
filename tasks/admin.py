from django.contrib import admin
from .models import Task, Comment

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('project', 'user', 'creation_date')

class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('task', 'user', 'creation_date')

admin.site.register(Task, TaskAdmin)
admin.site.register(Comment, CommentAdmin)
