from django.views import generic
from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task
from .forms import TaskCreateForm


class TasksListView(LoginRequiredMixin, generic.ListView):

    model = Task
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
    

class TaskCreateView(generic.edit.CreateView):

    model = Task
    form_class = TaskCreateForm
    template_name = 'tasks/create.html'

    def form_valid(self, form):
        user = self.request.user

        if user.is_verified:
            form.instance.user = user
            return super().form_valid(form)

    def get_success_url(self):
        return reverse('tasks:tasks')


class TaskUpdateView(generic.edit.UpdateView):
    pass


class TaskDeleteView(generic.edit.DeleteView):
    pass
