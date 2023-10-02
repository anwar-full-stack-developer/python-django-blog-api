from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tag, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name',)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name',)


class PostReadSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False, read_only=True)
    author = UserSerializer(required=False, read_only=True)
    serializers.ImageField(use_url=True, required=False, allow_null=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'tags', 'author', 'image',)
        

class PostSerializer(serializers.ModelSerializer):
    # tags = TagSerializer(many=True, required=False, read_only=True)
    # author = UserSerializer(required=False, read_only=True)
    serializers.ImageField(use_url=True, required=False, allow_null=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'tags', 'author', 'image',)
