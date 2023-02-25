from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from task_manager.models import Task


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
