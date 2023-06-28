# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import generics, permissions, filters
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend

# Internal:
from .serializers import EventSerializer
from pp5_api.permissions import IsUserOrReadOnly
from .models import Event
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class EventList(generics.ListCreateAPIView):
    """
    List and create Event by logged in user
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.annotate(
        comments_count=Count('comment', distinct=True),
        interested_count=Count('interested', distinct=True),
        join_request=Count('join', distinct=True),
    ).order_by('-created_on')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = {
        'owner__followed__owner__profile': ['exact'],
        'interested__owner__profile': ['exact'],
        'join__owner__profile': ['exact'],
        'owner__profile': ['exact'],
        'category': ['exact'],
        'event_start_date': ['lte'],
    }
    search_fields = [
        'owner__username',
        'title',
        'event_start_date',
        'category',
    ]
    ordering_fields = [
        'comments_count',
        'interested_count',
        'interested__created_on'
        'join_request',
        'join__created_on',
        'event_start_date',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an event, update or delete it by id if user owns it
    """
    serializer_class = EventSerializer
    permission_classes = [IsUserOrReadOnly]
    queryset = Event.objects.annotate(
        comments_count=Count('comment', distinct=True),
        interested_count=Count('interested', distinct=True),
        join_request=Count('join', distinct=True),
    ).order_by('-created_on')
