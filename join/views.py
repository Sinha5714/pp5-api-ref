from rest_framework import generics, permissions
from pp5_api.permissions import IsUserOrReadOnly
from .models import Join
from .serializers import JoinListSerializer
from django_filters.rest_framework import DjangoFilterBackend


class JoinListView(generics.ListCreateAPIView):
    """
    List join or create a join reason if logged in.
    """
    serializer_class = JoinListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Join.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['event']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
