from rest_framework import generics, permissions
from pp5_api.permissions import IsUserOrReadOnly
from .models import Interested
from .serializers import InterestedSerializer


class InterestedListView(generics.ListCreateAPIView):
    """
    List and add Interest to event by logged in user
    """
    serializer_class = InterestedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Interested.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class InterestedDetailView(generics.RetrieveDestroyAPIView):
    """
    Retrieve an interest or delete it by id if user owns it
    """
    serializer_class = InterestedSerializer
    permission_classes = [IsUserOrReadOnly]
    queryset = Interested.objects.all()
