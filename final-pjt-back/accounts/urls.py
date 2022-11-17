from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path("profile/<username>/", views.profile),
    path("<int:user_id>/follow/", views.follow),
    path("<nickname>/isfollow/", views.isFollow),
    path("<nickname>/followings", views.getFollowings),
    path("<nickname>/followers", views.getFollowers),
    path("<int:movie_id>/movies/islike/", views.movieIsLike),
    path("<int:comment_id>/comments/islike/", views.commentIsLike),
]
