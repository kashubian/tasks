from datetime import datetime, timedelta

from django.test import TestCase, Client
from django.shortcuts import reverse

from apps.tasks.models import Task
from apps.accounts.models import User


class TaskViewTestCase(TestCase):

    def setUp(self):
        self.now = datetime.now()
        self.admin = User.objects.create(email="test@test.pl")
        self.admin.set_password('12345')
        self.admin.is_verified = True
        self.admin.save()

        self.client = Client()
        logged_in = self.client.login(
            username='test@test.pl',
            password='12345'
        )
        
        self.new_task = Task.objects.create(
            title="test title",
            date=self.now,
            user=self.admin
        )

    def test_tasks_list(self):
        response = self.client.get(reverse('tasks:tasks'))
        assert response.status_code == 200
        