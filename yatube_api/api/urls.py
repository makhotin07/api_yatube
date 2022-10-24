from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import GroupsViewSet, PostsViewSet, CommentsViewSet

router = DefaultRouter()

router.register('groups', GroupsViewSet, basename='groups')
router.register('posts', PostsViewSet, basename='posts')
router.register('comment', CommentsViewSet, basename='comment')

urlpatterns = [
    path("v1/", include(router.urls)),
]
