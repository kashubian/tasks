from django.views import generic

from .models import Task


class TasksListView(generic.ListView):

    model = Task
    ordering = ['date']
    context_object_name = 'tasks'
    template_name = 'tasks/list.html'


class TaskDetailView(generic.DetailView):

    model = Task
    context_object_name = 'task'
    template_name = 'tasks/detail.html'
    