from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import MovieSerializer, CommentSerializer, GenreSerializer
from .models import Movie, Comment, Genre

# Create your views here.
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def movie_likes(request, movie_id):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_id)

        if movie.like_users.filter(pk=request.user.id).exists():
            movie.like_users.remove(request.user)
            is_liked = False
        else:
            movie.like_users.add(request.user)
            is_liked = True

        return Response({"is_liked": is_liked}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "로그인 후 이용가능합니다."}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'POST'])
def comment_list(request, movie_id):
    if request.method == 'GET':
        comments = Comment.objects.filter(movie_id=movie_id).order_by('created_at')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return Response({'message': '로그인 후 이용가능합니다.'}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie_id=movie_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        comment.delete()
        return Response({ 'id': comment_id }, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def genre_list(request):
    genres = get_list_or_404(Genre)
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)