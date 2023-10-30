from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name="post-detail", lookup_field="id", lookup_url_kwarg="pk")

    class Meta:
        model = Post
        fields = [
            "url",
            "id",
            "cover",
            "title",
            "description",
            "demo",
        ]


class ShortPostSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name="post-detail", lookup_field="id", lookup_url_kwarg="pk")

    class Meta:
        model = Post
        fields = [
            "url",
            "id",
            "cover",
            "title",
        ]
