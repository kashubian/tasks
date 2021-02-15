from django.views import generic
from django.shortcuts import reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from datetime import timedelta, datetime

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
    
    model = Task
    form_class = TaskCreateForm
    template_name = 'tasks/update.html'

    def get_success_url(self):
        return reverse('tasks:task', kwargs={"pk": self.object.id})


class TaskDeleteView(generic.edit.DeleteView):
    
    model = Task
    template_name = 'tasks/delete.html'

    def get_success_url(self):
        return reverse('tasks:tasks')

# reminders email is sent when it's less than 24 hours to the task's date
def send_reminders(request):
    tasks = Task.objects.all()
    time_now = datetime.now()

    for task in tasks:

        if (task.date < datetime.now() + timedelta(hours=24) 
            and task.sent_reminder == False):
            
            subject = task.title
            message = render_to_string('tasks/reminder_email.html',
                {
                'date': task.date,
                'description': task.description,
            })
            from_email = 'tasks@reminders.com'
            task.user.email_user(subject, message, from_email)
            task.sent_reminder = True
            task.save()

    return redirect('/')
