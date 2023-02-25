from django.urls import path

from task_manager.views import (
    index,
    CompletedTasksListView,
    TaskTypeListView,
    TaskTypeDetailView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
    TaskTypeCreateView,
    UncompletedTasksListView,
    TaskDetailView,
    TaskUpdateView,
)

urlpatterns = [
    path('', index, name='index'),
    path('tasks/completed/', CompletedTasksListView.as_view(), name='completed-tasks'),
    path('tasks/uncompleted/', UncompletedTasksListView.as_view(), name='uncompleted-tasks'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks_types/', TaskTypeListView.as_view(), name='task-types'),
    path('tasks_types/<int:pk>/', TaskTypeDetailView.as_view(), name='task-type-detail'),
    path('tasks_types/<int:pk>/update/', TaskTypeUpdateView.as_view(), name='task-type-update'),
    path('tasks_types/<int:pk>/delete/', TaskTypeDeleteView.as_view(), name='task-type-delete'),
    path('tasks_types/create/', TaskTypeCreateView.as_view(), name='task-type-create'),

]

app_name = 'task_manager'
