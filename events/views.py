from django.db.models import Count
from rest_framework import generics, filters
from .models import Event
from .serializers import EventSerializer
from pp5_api.permissions import IsUserOrReadOnly


class EventList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    serializer_class = EventSerializer
    queryset = Event.objects.annotate(
    ).order_by('-created_on')
