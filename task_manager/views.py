from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task_manager.models import Task, TaskType


@login_required
def index(request):
    num_completed_tasks = Task.objects.filter(is_completed=True).count()
    num_un_completed_tasks = Task.objects.filter(is_completed=False).count()
    num_workers = Task.objects.count()
    context = {
        'num_completed_tasks': num_completed_tasks,
        'num_workers': num_workers,
        'num_un_completed_tasks': num_un_completed_tasks,
    }
    return render(request, 'task_manager/index.html', context=context)


class CompletedTasksListView(generic.ListView, LoginRequiredMixin):
    model = Task
    queryset = Task.objects.filter(is_completed=True).select_related('task_type').prefetch_related('assignees')
    context_object_name = 'task_list'
    template_name = 'task_manager/tasks_list.html'


class UncompletedTasksListView(generic.ListView, LoginRequiredMixin):
    model = Task
    queryset = Task.objects.filter(is_completed=False).select_related('task_type').prefetch_related('assignees')
    context_object_name = 'task_list'
    template_name = 'task_manager/tasks_list.html'


class TaskTypeListView(generic.ListView, LoginRequiredMixin):
    model = TaskType
    context_object_name = 'task_types'
    template_name = 'task_manager/task_type_list.html'


class TaskTypeDetailView(generic.DetailView, LoginRequiredMixin):
    model = TaskType
    template_name = 'task_manager/task_type_detail.html'


class TaskTypeUpdateView(generic.UpdateView, LoginRequiredMixin):
    model = TaskType
    template_name = 'task_manager/task_type_form.html'
    fields = '__all__'
    success_url = reverse_lazy('task_manager:task-types')


class TaskTypeDeleteView(generic.DeleteView, LoginRequiredMixin):
    model = TaskType
    template_name = 'task_manager/task_type_confirm_delete.html'
    success_url = reverse_lazy('task_manager:task-types')


class TaskTypeCreateView(generic.CreateView, LoginRequiredMixin):
    model = TaskType
    template_name = 'task_manager/task_type_form.html'
    fields = '__all__'
    success_url = reverse_lazy('task_manager:task-types')


class TaskDetailView(generic.DetailView, LoginRequiredMixin):
    model = Task
    template_name = 'task_manager/task_detail.html'
