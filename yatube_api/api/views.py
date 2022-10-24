from django.shortcuts import get_object_or_404
from rest_framework import permissions

from rest_framework import viewsets

from posts.models import Group, Post
from .permissions import IsAuthorOrReadOnly
from serializers import CommentSerializer, GroupSerializer, PostSerializer


class GroupsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permissions_classes = [
        permissions.IsAuthenticated, IsAuthorOrReadOnly
    ]


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAuthorOrReadOnly
    ]

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)
