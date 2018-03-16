from django.db import models
from django.db.models import DateTimeField, DurationField, CharField
from django.utils import timezone


class FeedEvent(models.Model):
    started_at = DateTimeField(auto_now_add=True)
    duration = DurationField(null=True)
    user = CharField(max_length=255, null=False, blank=False)

    def stop(self):
        self.duration = timezone.now() - self.started_at
        return self
