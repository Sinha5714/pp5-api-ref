from rest_framework import generics, filters
from .serializers import ProfileSerializer
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from pp5_api.permissions import IsUserOrReadOnly
from .models import Profile


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        events_count=Count('user__event', distinct=True),
    ).order_by('-created_on')

    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'user__profile'
    ]
    ordering_fields = [
        'events_count',
    ]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a profile if you're the owner.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsUserOrReadOnly]
    queryset = Profile.objects.annotate(
    ).order_by('-created_on')
