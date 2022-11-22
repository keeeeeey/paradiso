from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import MovieSerializer, CommentSerializer, GenreSerializer, MovieSearchSerializer
from .models import Movie, Comment, Genre
from django.db.models import Q

# Create your views here.
@api_view(['GET'])
def movie_list(request, limit, offset):
    movies = get_list_or_404(Movie)[offset:limit]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def top_rated_movies(request):
    movies = Movie.objects.order_by("vote_average")[:20]
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
            movie_likes_count = movie.like_users.count()
        else:
            movie.like_users.add(request.user)
            is_liked = True
            movie_likes_count = movie.like_users.count()

        return Response({"is_liked": is_liked, "like_users_count": movie_likes_count}, status=status.HTTP_200_OK)
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
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user.is_authenticated:
        if request.method == 'PUT':
            if comment.user != request.user:
                return Response({"message": "작성자만 수정이 가능합니다."}, status=status.HTTP_403_FORBIDDEN)

            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            if comment.user != request.user:
                return Response({"message": "작성자만 삭제가 가능합니다."}, status=status.HTTP_403_FORBIDDEN)

            comment.delete()
            return Response({ 'id': comment_id }, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({"message": "로그인 후 이용가능합니다."}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def comment_likes(request, comment_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_id)

        if comment.like_users.filter(pk=request.user.id).exists():
            comment.like_users.remove(request.user)
            is_liked = False
            like_users_count = comment.like_users.count()
        else:
            comment.like_users.add(request.user)
            is_liked = True
            like_users_count = comment.like_users.count()

        return Response({"is_liked": is_liked, "like_users_count": like_users_count}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "로그인 후 이용가능합니다."}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def genre_list(request):
    genres = get_list_or_404(Genre)
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_movies_by_genre(request, genre, limit, offset):
    genre = Genre.objects.get(name=genre)
    movies = genre.movie_set.all()[offset:limit]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def do_search(request, keyWord):
    key_list = list(keyWord.split())

    the_movie = Movie.objects.filter(title=keyWord)

    search_result = set()
    for key in key_list:
        movies = Movie.objects.filter(Q(title__icontains=key) | 
                                      Q(overview__icontains=key)).distinct()
        for movie in movies:
            if the_movie and movie != the_movie[0]:
                search_result.add(movie)
    
    serializer = MovieSearchSerializer(search_result, many=True)

    if the_movie:
        the_movie_serializer = MovieSearchSerializer(the_movie[0])
        return Response({"the_movie_serializer" : the_movie_serializer.data, "serializer" : serializer.data})
    else:
        return Response({"the_movie_serializer" : "", "serializer" : serializer.data})