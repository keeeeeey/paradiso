from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ("id", "username", "email", "nickname")


class UserFavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ("favorite_movies",)


class ProfileSerializer(serializers.ModelSerializer):

    followings_count = serializers.IntegerField(source="followings.count", read_only=True)
    followers_count = serializers.IntegerField(source="followers.count", read_only=True)

    class Meta:
        model = get_user_model()
        fields = ("username", "email", "nickname", "followings_count", "followers_count", "id")


# jwt token 결과 커스텀 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)

        token = self.get_token(self.user)
        
        # response에 추가하고 싶은 key값들 추가
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['nickname'] = self.user.nickname
        data['refresh'] = str(token)
        data['access'] = str(token.access_token)
        data['isFirst'] = self.user.isFirst
        
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
