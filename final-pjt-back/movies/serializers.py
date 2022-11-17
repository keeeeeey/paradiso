from rest_framework import serializers
from .models import Movie, Comment, Genre
from accounts.serializers import UserSerializer


class MovieSerializer(serializers.ModelSerializer):
    like_users_count = serializers.IntegerField(source="like_users.count", read_only=True)
    comment_count = serializers.IntegerField(source="comment_set.count", read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"
        read_only_fields = ("like_users",)


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    like_users_count = serializers.IntegerField(source="like_users.count", read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("movie", "like_users",)


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = "__all__"