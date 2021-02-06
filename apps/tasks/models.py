from django.db import models
from apps.core.models import Timestamp
from apps.accounts.models import User
import uuid


class Task(Timestamp):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return (self.title)

    class Meta:
        ordering = ['date']
