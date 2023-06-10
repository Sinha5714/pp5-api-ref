from django.db import models
from django.contrib.auth.models import User
from events.models import Event


class Interested(models.Model):
    """
    Class model for Interested, related to user and events
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(
        Event, related_name='interested', on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.user} {self.event}'
