from rest_framework import generics, permissions
from pp5_api.permissions import IsUserOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentListView(generics.ListCreateAPIView):
    """
    Model for list of comments or create comments for logged in users
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsUserOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
