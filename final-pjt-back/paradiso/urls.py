from django.contrib import admin
from django.urls import path, include
from accounts.serializers import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include("movies.urls")),
    path('accounts/', include('accounts.urls')),
    path("api/token/", MyTokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path("api/token/verify/", TokenVerifyView.as_view()),
]
