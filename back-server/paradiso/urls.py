from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include("accounts.urls")),
    path('movies/', include("movies.urls")),
    path('accounts/', include('accounts.urls')),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
]
