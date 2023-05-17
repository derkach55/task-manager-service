from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic, View

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


class TasksListView(LoginRequiredMixin, generic.ListView):
    model = Task
    queryset = Task.objects.select_related('task_type').prefetch_related('assignees').order_by(
        'is_completed', 'deadline')
    context_object_name = 'task_list'
    template_name = 'task_manager/tasks_list.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(TasksListView, self).get_context_data()
        name = self.request.GET.get('name', '')
        context['search_field'] = TaskSearchForm(initial={'name': name})

        return context

    def get_queryset(self) -> QuerySet:
        queryset = super(TasksListView, self).get_queryset()
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    context_object_name = 'task_types'
    template_name = 'task_manager/task_type_list.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(TaskTypeListView, self).get_context_data()
        name = self.request.GET.get('name', '')
        context['search_field'] = TaskTypeSearchForm(initial={'name': name})

        return context

    def get_queryset(self) -> QuerySet:
        queryset = super(TaskTypeListView, self).get_queryset()
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class TaskTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaskType
    template_name = 'task_manager/task_type_detail.html'


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    template_name = 'task_manager/task_type_form.html'
    fields = '__all__'
    success_url = reverse_lazy('task_manager:task-types')


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    template_name = 'task_manager/task_type_confirm_delete.html'
    success_url = reverse_lazy('task_manager:task-types')


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    template_name = 'task_manager/task_type_form.html'
    fields = '__all__'
    success_url = reverse_lazy('task_manager:task-types')


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = 'task_manager/task_detail.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super(TaskDetailView, self).get_context_data()
        context['date'] = timezone.now()
        return context


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_manager:tasks-list')


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy('task_manager:tasks-list')


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_manager:tasks-list')


class ChangeTaskStatusView(LoginRequiredMixin, View):

    def post(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        task.is_completed = not task.is_completed
        task.save()
        return HttpResponseRedirect(reverse_lazy('task_manager:task-detail', args=[pk]))


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(PositionListView, self).get_context_data()
        name = self.request.GET.get('name', '')
        context['search_field'] = PositionSearchForm(initial={'name': name})

        return context

    def get_queryset(self) -> QuerySet:
        queryset = super(PositionListView, self).get_queryset()
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class PositionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = '__all__'
    success_url = reverse_lazy('task_manager:position-list')


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy('task_manager:position-list')


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = '__all__'
    success_url = reverse_lazy('task_manager:position-list')


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(WorkerListView, self).get_context_data()
        user_name = self.request.GET.get('user_name', '')
        context['search_field'] = WorkerSearchForm(initial={'user_name': user_name})

        return context

    def get_queryset(self) -> QuerySet:
        queryset = super(WorkerListView, self).get_queryset()
        user_name = self.request.GET.get('user_name')
        if user_name:
            queryset = queryset.filter(username__icontains=user_name)

        return queryset


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    fields = ['position']
    success_url = reverse_lazy('task_manager:worker-list')


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy('task_manager:worker-list')


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
