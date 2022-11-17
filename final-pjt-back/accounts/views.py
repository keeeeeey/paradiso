from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, get_list_or_404
from movies.serializers import MovieSerializer, CommentSerializer

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
def profile(request, username):
    User = get_user_model()
    person = get_object_or_404(User, username=username)
    profileSerializer = ProfileSerializer(person)

    movies = person.like_movies.all()
    movieSerializer = MovieSerializer(movies, many=True)

    comments = person.comment_set.all()
    commentSerializer = CommentSerializer(comments, many=True)

    serializer = {
        "userSerializer": profileSerializer.data,
        "movieSerializer": movieSerializer.data,
        "commentSerializer": commentSerializer.data,
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
            else:
                person.followers.add(request.user)
                is_followed = True

        return Response({'is_followed': is_followed}, status=status.HTTP_200_OK)
    else:
        return Response({'message': '로그인 후 이용가능합니다.'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def isLike(request, movie_id):
    if request.user.is_authenticated:
        if request.user.like_movies.filter(pk=movie_id).exists():
            return Response({'is_liked': True})
        else:
            return Response({'is_liked': False})
    else:
        return Response({'is_liked': False})