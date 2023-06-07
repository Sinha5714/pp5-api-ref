from django.db.models import Count
from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
    ).order_by('-created_on')


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a profile if you're the owner.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
    ).order_by('-created_on')
