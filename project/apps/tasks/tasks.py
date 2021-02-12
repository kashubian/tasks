from workers import task
from datetime import datetime, timedelta
from apps.tasks.models import Task
from django.template.loader import render_to_string


@task(schedule=60*60)
def send_reminders():
    tasks = Task.objects.filter(sent_remainder=False)
    time_now = datetime.now()

    for task in tasks:

        if task.date < datetime.now() + timedelta(hours=24):
            
            subject = task.title
            message = render_to_string('tasks/remainder_email.html',
                {
                'date': task.date,
                'description': task.description,
            })
            from_email = 'tasks@remainders.com'
            task.user.email_user(subject, message, from_email)
            task.sent_remainder = True
            task.save()
