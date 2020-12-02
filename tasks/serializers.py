from rest_framework import serializers
from accounts.serializers import UserSerializer

from .models import Task, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'creation_date']

class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    comments = CommentSerializer(many = True)

    class Meta:
        model = Task
        fields = ['id', 'name', 'user', 'project', 'text', 'creation_date', 'comments']