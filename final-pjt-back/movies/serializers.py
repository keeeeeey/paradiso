from rest_framework import serializers
from .models import Movie, Comment, Genre
from accounts.serializers import UserSerializer


class MovieSerializer(serializers.ModelSerializer):
    like_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ('user', 'content',)


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = "__all__"