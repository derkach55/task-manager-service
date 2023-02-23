from django.contrib.auth.models import AbstractUser
from django.db import models


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.username}({self.first_name} {self.last_name}): {self.position}"


class Task(models.Model):
    PRIORITY_CHOICES = (
        ('Urgent', 'Urgent Priority'),
        ('Low', 'Low Priority'),
        ('Medium', 'Medium Priority'),
        ('High', 'High Priority'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='Medium')
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker, related_name='tasks')

    def __str__(self):
        return self.name
