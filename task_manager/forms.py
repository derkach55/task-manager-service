from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from task_manager.models import Task, Worker


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = ['name', 'task_type', 'description', 'deadline', 'priority', 'assignees']


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + ('position', 'first_name', 'last_name', 'email',)


class TaskTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Name'})
    )


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Name'})
    )


class PositionSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Name'})
    )


class WorkerSearchForm(forms.Form):
    user_name = forms.CharField(
        max_length=255,
        required=False,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Username'})
    )
