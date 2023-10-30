from django.urls import path
from .views import (
    PostDetailAPIView,
    PostListAPIView,
)
urlpatterns = [
    path("", view=PostListAPIView.as_view(), name="post-list"),
    path("post/<uuid:pk>/", view=PostDetailAPIView.as_view(), name="post-detail"),
]