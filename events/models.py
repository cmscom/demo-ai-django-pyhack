from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    display_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.display_name

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')
    event_date = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    participants = models.ManyToManyField(User, through='EventParticipation', related_name='participating_events')

    def __str__(self):
        return self.name

class EventParticipation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('event', 'participant')

