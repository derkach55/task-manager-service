from django import forms
from django.contrib.auth import get_user_model

from task_manager.models import Task


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = ['name', 'task_type', 'description', 'deadline', 'priority', 'assignees']
