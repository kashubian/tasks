from django.db import models
from apps.core.models import Timestamp
from apps.accounts.models import User
import uuid
from datetime import datetime, timedelta


class Task(Timestamp):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField()
    sent_reminder = models.BooleanField(default=False)
    remind_at = models.DateTimeField(null=True)

    def __str__(self):
        return (self.title)

    def set_default_remind_time(self):
        return self.date - timedelta(hours=24)

    def save(self, *args, **kwargs):
        if self.remind_at is None:
            self.remind_at = self.set_default_remind_time()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['date']
