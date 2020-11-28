from django import forms

from .models import Task
from labels.models import Label

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'text', 'project', 'labels']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UpdateTaskForm, self).__init__(*args, **kwargs)

        self.fields['labels'].queryset = Label.objects.filter(user = self.request.user)

    labels = forms.ModelMultipleChoiceField(
            queryset = None,
            widget = forms.CheckboxSelectMultiple,
        )