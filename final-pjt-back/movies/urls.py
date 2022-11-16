from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_id>/comments/', views.comment_list),
    path('<int:movie_id>/comments/<int:comment_id>/', views.comment),
    path('genres/', views.genre_list),
]
