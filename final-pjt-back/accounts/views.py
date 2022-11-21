from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, get_list_or_404
from movies.serializers import MovieSerializer, CommentSerializer
from movies.models import Movie, Genre
import json

from .serializers import UserSerializer, ProfileSerializer


@api_view(['POST'])
def signup(request):
    password = request.data.get("password")
    password_confirm = request.data.get("passwordConfirm")

    if password != password_confirm:
        return Response(("error : 비밀번호가 일치하지 않습니다."), status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        # 사용자의 암호를 해쉬함수를 통해 바꿔줌(암호화)
        user.set_password(request.data.get("password"))
        # 바꾼 비밀번호로 다시 저장
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def profile(request, nickname):
    User = get_user_model()
    person = get_object_or_404(User, nickname=nickname)
    profileSerializer = ProfileSerializer(person)

    movies = person.like_movies.all()
    movieSerializer = MovieSerializer(movies, many=True)

    comments = person.comment_set.all()
    commentSerializer = CommentSerializer(comments, many=True)

    like_comments = person.like_comments.all()
    likeCommentSerializer = CommentSerializer(like_comments, many=True)

    serializer = {
        "userSerializer": profileSerializer.data,
        "movieSerializer": movieSerializer.data,
        "commentSerializer": commentSerializer.data,
        "likeCommentSerializer": likeCommentSerializer.data,
    }

    return Response({"serializer": serializer})


@api_view(['POST'])
def follow(request, user_id):
    if request.user.is_authenticated:
        User = get_user_model()
        person = User.objects.get(pk=user_id)
        if person != request.user:
            if person.followers.filter(pk=request.user.pk).exists():
                person.followers.remove(request.user)
                is_followed = False
                followers_count = person.followers.count()
            else:
                person.followers.add(request.user)
                is_followed = True
                followers_count = person.followers.count()

            return Response({'is_followed': is_followed, 'followers_count': followers_count}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "자기 자신은 팔로우 할 수 없습니다."}, status=status.HTTP_200_OK)
    else:
        return Response({'message': '로그인 후 이용가능합니다.'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def movieIsLike(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.user.is_authenticated:
        like_count = movie.like_users.count()
        if request.user.like_movies.filter(pk=movie_id).exists():
            return Response({'is_liked': True, 'like_count': like_count})
        else:
            return Response({'is_liked': False, 'like_count': like_count})


@api_view(['GET'])
def commentIsLike(request, comment_id):
    if request.user.is_authenticated:
        if request.user.like_comments.filter(pk=comment_id).exists():
            return Response({'is_liked': True})
        else:
            return Response({'is_liked': False})


@api_view(['GET'])
def isFollow(request, nickname):
    if request.user.is_authenticated:
        if request.user.nickname == nickname:
            is_mypage = True
        else:
            is_mypage = False

        if request.user.followings.filter(nickname=nickname).exists():
            return Response({'is_followed': True, 'is_mypage': is_mypage})
        else:
            return Response({'is_followed': False, 'is_mypage': is_mypage})


@api_view(['GET'])
def getFollowings(request, nickname):
    User = get_user_model()
    person = User.objects.get(nickname=nickname)
    followings = person.followings.all()
    serializer = UserSerializer(followings, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getFollowers(request, nickname):
    User = get_user_model()
    person = User.objects.get(nickname=nickname)
    followers = person.followers.all()
    serializer = UserSerializer(followers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def idCheck(request, username):
    User = get_user_model()

    if User.objects.filter(username=username).exists():
        return Response({"id_exist" : True})
    else:
        return Response({"id_exist" : False})
    

@api_view(['GET'])
def emailCheck(request, email):
    User = get_user_model()

    if User.objects.filter(email=email).exists():
        return Response({"email_exist" : True})
    else:
        return Response({"email_exist" : False})


@api_view(['GET'])
def nicknameCheck(request, nickname):
    User = get_user_model()

    if User.objects.filter(nickname=nickname).exists():
        return Response({"nickname_exist" : True})
    else:
        return Response({"nickname_exist" : False})


@api_view(['POST'])
def createFavorite(request):
    if request.user.is_authenticated:
        for movie in request.data["my_favorite"]:
            request.user.favorite_movies.add(movie)
            request.user.isFirst = False
            request.user.save()

    return Response({"message" : "좋아하는 영화 등록 성공"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def userFavorites(request):
    my_favorites = request.user.favorite_movies.all()
    my_genres = []
    similar_movies = set()
    for favorite in my_favorites:
        movie = get_object_or_404(Movie, pk=favorite.id)
        for genre in movie.genres.all():
            if genre.id not in my_genres:
                my_genres.append(genre.id)
                temp_genre = Genre.objects.get(pk=genre.id)
                similar_list = temp_genre.movie_set.order_by("?")
                for i in range(3):
                    similar_movies.add(similar_list[i])

    serializer = MovieSerializer(similar_movies, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def mostFavorite(request):
    movies = Movie.objects.all()
    most_favorite_movies = []

    for movie in movies:
        most_favorite_movies.append([movie.favorite_user.count(), movie])

    most_favorite_movies.sort(key=lambda x: -x[0])

    most_favorite_movies_object = []
    for i in range(10):
        most_favorite_movies_object.append(most_favorite_movies[i][1])

    serializer = MovieSerializer(most_favorite_movies_object, many=True)
    
    return Response(serializer.data)