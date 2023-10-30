from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.views.decorators.cache import cache_page
from .models import Post
from .serializers import PostSerializer, ShortPostSerializer
from rest_framework.response import Response
from rest_framework import status
from apps.ufc_base.pagination import *
# Create your views here.


class PostDetailAPIView(APIView):
    permission_classes = (AllowAny, )

    #@method_decorator(cache_page(7200))
    def get(self, request, *args, **kwargs):
        post = Post.objects.get(id=self.kwargs["pk"])
        if post:
            serializer = PostSerializer(post, read_only=True, context={"request": request})
            return Response(data={"post": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(data={"error": "This post wasn't found :("}, status=status.HTTP_404_NOT_FOUND)


class PostListAPIView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        if posts.exists():
            paginator = LargeSetPagination()
            results = paginator.paginate_queryset(queryset=posts, request=request)
            serializer = ShortPostSerializer(results, many=True, context={"request": request})
            return paginator.get_paginated_response(data={"posts": serializer.data})
        else:
            return Response(data={"error": "No content"}, status=status.HTTP_204_NO_CONTENT)
