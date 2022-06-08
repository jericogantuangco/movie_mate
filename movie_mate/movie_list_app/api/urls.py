from django.urls import path, include
from movie_list_app.api.views import MovieList, MovieDetails

urlpatterns = [
    path('list/', MovieList.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetails.as_view(), name='movie-details')
]
