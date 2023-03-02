from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from task_manager.models import Worker, Position, TaskType, Task

admin.site.register(Position)
admin.site.register(TaskType)
admin.site.register(Task)


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position", )
