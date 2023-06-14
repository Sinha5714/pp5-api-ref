# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User

# Internal:
from events.models import Event
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Join(models.Model):
    """
    A class for the Join model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(
        Event, related_name='join', on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255, default='', blank=False)
    email = models.EmailField(max_length=255, default='',blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['user', 'event']

    def __str__(self):
        return f'{self.user} requested to join {self.event}'
