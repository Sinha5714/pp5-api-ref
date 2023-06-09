# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

# Internal:
from pp5_api.permissions import IsUserOrReadOnly
from .models import Join
from .serializers import JoinSerializer
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class JoinListView(generics.ListCreateAPIView):
    """
    List join or create a join reason if logged in.
    """
    serializer_class = JoinSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Join.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['event']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class JoinDetailView(generics.RetrieveDestroyAPIView):
    """
    Retrieve a join request or delete it by id.
    """
    permission_classes = [IsUserOrReadOnly]
    serializer_class = JoinSerializer
    queryset = Join.objects.all()
