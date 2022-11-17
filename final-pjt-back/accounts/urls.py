from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path("profile/<username>/", views.profile),
    path("<int:user_id>/follow/", views.follow),
    path("<int:movie_id>/islike/", views.isLike),
]
