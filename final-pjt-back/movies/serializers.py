from rest_framework import serializers
from .models import Movie, Comment, Genre
from accounts.serializers import UserSerializer


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(read_only=True, many=True)
    like_users_count = serializers.IntegerField(source="like_users.count", read_only=True)
    comment_count = serializers.IntegerField(source="comment_set.count", read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"
        read_only_fields = ("like_users",)


class MovieTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ("id", "title",)


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    like_users_count = serializers.IntegerField(source="like_users.count", read_only=True)
    movie = MovieTitleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("like_users",)