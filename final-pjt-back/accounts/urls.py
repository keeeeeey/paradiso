from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path("idcheck/<username>/", views.idCheck),
    path("emailcheck/<email>/", views.emailCheck),
    path("nicknamecheck/<nickname>/", views.nicknameCheck),
    path("profile/<nickname>/", views.profile),
    path("<int:user_id>/follow/", views.follow),
    path("<nickname>/isfollow/", views.isFollow),
    path("<nickname>/followings/", views.getFollowings),
    path("<nickname>/followers/", views.getFollowers),
    path("<int:movie_id>/movies/islike/", views.movieIsLike),
    path("<int:comment_id>/comments/islike/", views.commentIsLike),
    path("addfavoritemovies/", views.createFavorite),
    path("userfavorites/", views.userFavorites),
    path('mostfavorite/', views.mostFavorite),
    path('<nickname>/getfollowings/', views.getFollowings),
    path('<nickname>/getfollowers/', views.getFollowers),
]
