from django.urls import path

from .views import PostListCreateAPIView, PostDetailsAPIView



urlpatterns = [
    path('posts/api/', PostListCreateAPIView.as_view(), name='api-post-list'),
    path('posts/api/<int:id>/', PostDetailsAPIView.as_view(), name='api-post-details'),
]