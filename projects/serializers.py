from rest_framework import serializers

from .models import Project

from accounts.serializers import UserSerializer

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'user', 'creation_date']