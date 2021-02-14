from django import forms
from .models import Task


class TaskCreateForm(forms.ModelForm):
    date = forms.DateTimeField(
        input_formats = ['%Y-%m-%dT%H:%M'], 
        widget = forms.DateTimeInput(
        attrs={
            'type': 'datetime-local',
            'class': 'form-control'
            },
        format='%Y-%m-%dT%H:%M')
        )

    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'date'
        ]
        