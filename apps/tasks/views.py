from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task


class TasksListView(LoginRequiredMixin, generic.ListView):

    model = Task
    ordering = ['date']
    context_object_name = 'tasks'
    template_name = 'tasks/list.html'

    def get_queryset(self):
        user = self.request.user
        tasks = Task.objects.filter(user=user)
        return tasks
    

class TaskDetailView(generic.DetailView):

    model = Task
    context_object_name = 'task'
    template_name = 'tasks/detail.html'
    