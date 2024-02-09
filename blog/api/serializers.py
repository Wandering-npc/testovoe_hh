from rest_framework import serializers
from .models import Post, User


class UserSerializer(serializers.ModelSerializer):
      "Сериализатор юзера"
    
      class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")


class PostSerializer(serializers.ModelSerializer):
    "Сериализатор постов"
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
