from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer


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
