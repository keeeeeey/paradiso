from django.urls import path
from . import views

urlpatterns = [
    path('<int:limit>/<int:offset>/', views.movie_list),
    path('toprated/', views.top_rated_movies),
    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_id>/likes/', views.movie_likes),
    path('<int:movie_id>/comments/', views.comment_list),
    path('comments/<int:comment_id>/', views.comment),
    path('comments/<int:comment_id>/likes/', views.comment_likes),
    path('genres/', views.genre_list),
    path('genre/<genre>/<int:limit>/<int:offset>/', views.get_movies_by_genre),
    path('search/<keyWord>', views.do_search),
    path('similar/<int:movie_id>/', views.find_similar_movie)
]
