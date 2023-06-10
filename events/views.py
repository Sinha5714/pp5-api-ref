from rest_framework import generics, permissions, filters
from .serializers import EventSerializer
from pp5_api.permissions import IsUserOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event


class EventList(generics.ListCreateAPIView):
    """
    List and create Event by logged in user
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.annotate(
        comments_count=Count('comment', distinct=True),
        interested_count=Count('interested', distinct=True),
    ).order_by('-created_on')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = {
        'user__profile': ['exact'],
        'category': ['exact'],
    }
    search_fields = [
        'user__username',
        'title',
        'event_start_date',
        'category',
    ]
    ordering_fields = [
        'comments_count',
        'interested_count',
        'event_start_date',
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an event, update or delete it by id if user owns it
    """
    serializer_class = EventSerializer
    permission_classes = [IsUserOrReadOnly]
    queryset = Event.objects.annotate(
        comments_count=Count('comment', distinct=True),
        interested_count=Count('interested', distinct=True),
    ).order_by('-created_on')
