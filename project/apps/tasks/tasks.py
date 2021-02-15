from workers import task
from datetime import datetime, timedelta
from apps.tasks.models import Task
from django.template.loader import render_to_string


@task(schedule=60*60)
def send_reminders():
    tasks = Task.objects.filter(sent_reminder=False)

    for task in tasks:

        if task.remind_at < datetime.now():
            
            subject = task.title
            message = render_to_string('tasks/reminder_email.html',
                {
                'date': task.date,
                'description': task.description,
            })
            from_email = 'noreply@reminders.com'
            task.user.email_user(subject, message, from_email)
            task.sent_reminder = True
            task.save()
