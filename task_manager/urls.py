from django.urls import path

from task_manager.views import (
    index,
    TasksListView,
    TaskTypeListView,
    TaskTypeDetailView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
    TaskTypeCreateView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView,
    TaskCreateView,
    change_task_is_completed,
)

urlpatterns = [
    path('', index, name='index'),
    path('tasks/', TasksListView.as_view(), name='tasks-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('tasks_types/', TaskTypeListView.as_view(), name='task-types'),
    path('tasks_types/<int:pk>/', TaskTypeDetailView.as_view(), name='task-type-detail'),
    path('tasks_types/<int:pk>/update/', TaskTypeUpdateView.as_view(), name='task-type-update'),
    path('tasks_types/<int:pk>/delete/', TaskTypeDeleteView.as_view(), name='task-type-delete'),
    path('tasks_types/create/', TaskTypeCreateView.as_view(), name='task-type-create'),
    path('tasks/<int:pk>/mark_as_done/', change_task_is_completed, name='change_is_completed'),
]

app_name = 'task_manager'
