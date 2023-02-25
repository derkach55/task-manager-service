from django.urls import path

from task_manager.views import index, CompletedTasksListView, TaskTypeListView

urlpatterns = [
    path('', index, name='index'),
    path('tasks/completed/', CompletedTasksListView.as_view(), name='completed-tasks'),
    path('tasks_types/', TaskTypeListView.as_view(), name='task-types'),
]

app_name = 'task_manager'
