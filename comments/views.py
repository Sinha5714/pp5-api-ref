# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

# Internal:
from .models import Comment
from pp5_api.permissions import IsUserOrReadOnly
from .serializers import CommentSerializer, CommentDetailSerializer
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class CommentListView(generics.ListCreateAPIView):
    """
    Model for list of comments or create comments for logged in users
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['event']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsUserOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
