from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy, reverse

from todo.forms import TaskForm
from todo.models import Task


# def task_list(request):
#     tasks = Task.objects.all()
#     return render(request, 'todo/task_list.html', {'tasks': tasks})


# def add_task(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('task_list')
#     else:
#         form = TaskForm()
#     return render(request, 'todo/add_task.html', {'form': form})
                                

# def detail_task(request, task_id):
#     task = get_object_or_404(Task, pk=task_id)
#     return render(request,  'todo/detail_task.html', {'task': task})


# def edit_task(request, task_id):
#     task = get_object_or_404(Task, pk=task_id)
#     if request.method == 'POST':
#         form = TaskForm(request.POST, instance=task)
#         if form.is_valid():
#             form.save()
#             return redirect(detail_task, task_id=task.id)
#     else:
#         form = TaskForm(instance=task)
#     return render(request,  'todo/add_task.html', {'form': form})

class TaskModelMixin:
    model = Task


class TaskCreateUpdateMixin:    
    form_class = TaskForm
    template_name = 'todo/add_task.html'


class TaskListView(TaskModelMixin, ListView):
    template_name = 'todo/task_list.html'
    context_object_name = 'tasks'


class TaskCreateView(CreateView, TaskCreateUpdateMixin, TaskModelMixin): 
    success_url = reverse_lazy('task_list')


class TaskDetailView(TaskModelMixin, DetailView):
    template_name =  'todo/detail_task.html'
    pk_url_kwarg = 'task_id'


class TaskUpdateView(TaskModelMixin, TaskCreateUpdateMixin, UpdateView):
    pk_url_kwarg = 'task_id'

    def get_success_url(self) -> str:
        return reverse('detail_task', kwargs={'task_id': self.object.id})
