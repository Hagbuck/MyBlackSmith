from rest_framework import serializers

from .models import Label

from accounts.serializers import UserSerializer
from projects.serializers import ProjectSerializer

class LabelSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    project = ProjectSerializer()

    class Meta:
        model = Label
        fields = ['id', 'name', 'color', 'user', 'project', 'creation_date']