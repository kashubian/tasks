from datetime import datetime, timedelta

from freezegun import freeze_time

from django.test import TestCase

from apps.accounts.models import User
from apps.tasks.models import Task


@freeze_time("2021-02-15")
class TaskModelTestCase(TestCase):

    def setUp(self):

        self.now = datetime.now()
        self.week_ago = self.now - timedelta(weeks=1)
        admin = User.objects.create(
            email="test@test.pl"
        )
        
        self.default_remind_time = Task.objects.create(
            title="test title",
            date=self.now,
            user=admin
        )

        self.provided_remind_time = Task.objects.create(
            title="provided",
            date=self.now,
            user=admin,
            remind_at=self.week_ago
        )

    def test_default_remind_time(self):
        assert self.default_remind_time.remind_at == self.now - timedelta(hours=24)
        
    def test_provided_remind_time(self):
        assert self.provided_remind_time.remind_at == self.week_ago
        
    def test_str_title(self):
        assert self.default_remind_time.title == self.default_remind_time.__str__()
