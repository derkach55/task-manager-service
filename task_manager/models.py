from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.username}({self.first_name} {self.last_name}): {self.position}"

    def get_absolute_url(self):
        return reverse('task_manager:worker-detail', args=[self.pk])

    class Meta:
        ordering = ['username']


class Task(models.Model):
    PRIORITY_CHOICES = (
        ('Urgent', 'Urgent Priority'),
        ('High', 'High Priority'),
        ('Medium', 'Medium Priority'),
        ('Low', 'Low Priority'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='Medium')
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker, related_name='tasks')

    class Meta:
        ordering = ['is_completed', '-priority']

    def __str__(self):
        return self.name
