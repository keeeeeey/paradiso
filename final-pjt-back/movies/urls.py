from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_id>/likes/', views.movie_likes),
    path('<int:movie_id>/comments/', views.comment_list),
    path('comments/<int:comment_id>/', views.comment),
    path('comments/<int:comment_id>/likes/', views.comment_likes),
    path('genres/', views.genre_list),
]
