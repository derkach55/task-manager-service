from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task_manager.forms import TaskForm, WorkerCreationForm, TaskTypeSearchForm, TaskSearchForm, PositionSearchForm, \
    WorkerSearchForm
from task_manager.models import Task, TaskType, Position, Worker


@login_required
def index(request):
    num_completed_tasks = Task.objects.filter(is_completed=True).count()
    num_un_completed_tasks = Task.objects.filter(is_completed=False).count()
    num_workers = Worker.objects.count()
    context = {
        'num_completed_tasks': num_completed_tasks,
        'num_workers': num_workers,
        'num_un_completed_tasks': num_un_completed_tasks,
    }
    return render(request, 'task_manager/index.html', context=context)


class TasksListView(generic.ListView, LoginRequiredMixin):
    model = Task
    queryset = Task.objects.select_related('task_type').prefetch_related('assignees').order_by(
        'is_completed', 'deadline')
    context_object_name = 'task_list'
    template_name = 'task_manager/tasks_list.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TasksListView, self).get_context_data()
        name = self.request.GET.get('name', '')
        context['search_field'] = TaskSearchForm(initial={'name': name})

        return context

    def get_queryset(self):
        queryset = super(TasksListView, self).get_queryset()
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class TaskTypeListView(generic.ListView, LoginRequiredMixin):
    model = TaskType
    context_object_name = 'task_types'
    template_name = 'task_manager/task_type_list.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskTypeListView, self).get_context_data()
        name = self.request.GET.get('name', '')
        context['search_field'] = TaskTypeSearchForm(initial={'name': name})

        return context

    def get_queryset(self):
        queryset = super(TaskTypeListView, self).get_queryset()
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


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


class TaskUpdateView(generic.UpdateView, LoginRequiredMixin):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_manager:tasks-list')


class TaskDeleteView(generic.DeleteView, LoginRequiredMixin):
    model = Task
    success_url = reverse_lazy('task_manager:tasks-list')


class TaskCreateView(generic.CreateView, LoginRequiredMixin):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_manager:tasks-list')


@login_required
def change_task_is_completed(request, pk):
    task = Task.objects.get(id=pk)
    task.is_completed = not task.is_completed
    task.save()
    return HttpResponseRedirect(reverse_lazy('task_manager:task-detail', args=[pk]))


class PositionListView(generic.ListView, LoginRequiredMixin):
    model = Position
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PositionListView, self).get_context_data()
        name = self.request.GET.get('name', '')
        context['search_field'] = PositionSearchForm(initial={'name': name})

        return context

    def get_queryset(self):
        queryset = super(PositionListView, self).get_queryset()
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class PositionDetailView(generic.DetailView, LoginRequiredMixin):
    model = Position


class PositionUpdateView(generic.UpdateView, LoginRequiredMixin):
    model = Position
    fields = '__all__'
    success_url = reverse_lazy('task_manager:position-list')


class PositionDeleteView(generic.DeleteView, LoginRequiredMixin):
    model = Position
    success_url = reverse_lazy('task_manager:position-list')


class PositionCreateView(generic.CreateView, LoginRequiredMixin):
    model = Position
    fields = '__all__'
    success_url = reverse_lazy('task_manager:position-list')


class WorkerListView(generic.ListView, LoginRequiredMixin):
    model = Worker
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerListView, self).get_context_data()
        user_name = self.request.GET.get('user_name', '')
        context['search_field'] = WorkerSearchForm(initial={'user_name': user_name})

        return context

    def get_queryset(self):
        queryset = super(WorkerListView, self).get_queryset()
        user_name = self.request.GET.get('user_name')
        if user_name:
            queryset = queryset.filter(username__icontains=user_name)

        return queryset


class WorkerDetailView(generic.DetailView, LoginRequiredMixin):
    model = Worker


class WorkerUpdateView(generic.UpdateView, LoginRequiredMixin):
    model = Worker
    fields = ['position']
    success_url = reverse_lazy('task_manager:worker-list')


class WorkerDeleteView(generic.DeleteView, LoginRequiredMixin):
    model = Worker
    success_url = reverse_lazy('task_manager:worker-list')


class WorkerCreateView(generic.CreateView, LoginRequiredMixin):
    model = Worker
    form_class = WorkerCreationForm
