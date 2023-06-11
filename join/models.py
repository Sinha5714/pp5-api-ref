from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile
from events.models import Event


class Join(models.Model):
    """
    A class for the Join model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    reason = models.TextField(max_length=255)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.profile.name} for {self.event.title} : {self.reason}'
