# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import generics, permissions

# Internal:
from pp5_api.permissions import IsUserOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class FollowerListView(generics.ListCreateAPIView):
    """
    List follows or follow another user for logged in user
    """
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetailView(generics.RetrieveDestroyAPIView):
    """
    Retrieve a follower
    Destroy a follower, i.e. unfollow someone if following
    """
    permission_classes = [IsUserOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
