# Create your views here.

import requests
from django.shortcuts import redirect
from django.shortcuts import render
from django_filters.views import FilterView
from django_tables2 import SingleTableView

from .filters import MovieFilter
from .models import Movie
from .tables import MovieTable


# from .tables import MovieTable, MovieFilter

def clear_filters(request):
    return redirect('movies-list')

def fetch_and_save_movies(request):
    url = 'http://127.0.0.1:3000/movies'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
    else:
        data = None
        error_message = f"Failed to fetch data from the URL. Status code: {response.status_code}"
        return render(request, 'error.html', {'error_message': error_message})

    if data:
        for movie_data in data:
            date = movie_data.get('date')
            movies = movie_data.get('movies')
            for movie in movies:
                genre_str = movie['genre']
                genres_list = [word for line in genre_str for word in line.split()]
                print('genre_str', genre_str, type(genre_str), 'genres_list', genres_list)
                movie_instance = Movie(
                    title=movie['title'],
                    date=date,
                    year=movie['year'],
                    rated=movie['rated'],
                    released=movie['released'],
                    runtime=movie['runtime'],
                    genre=genres_list,
                    director=movie['director'],
                    writer=movie['writer'],
                    actors=movie['actors'],
                    plot=movie['plot'],
                    language=movie['language'],
                    country=movie['country'],
                    awards=movie['awards'],
                    poster=movie['poster'],
                    meta_score=movie['meta_score'],
                    imdb_rating=movie['imdb_rating'],
                    imdb_votes=movie['imdb_votes'],
                    imdb_id=movie['imdb_id'],
                    type=movie['type'],
                    dvd=movie['dvd'],
                    box_office=movie['box_office'],
                    production=movie['production'],
                    website=movie['website']
                )
                movie_instance.save()
                # movie_instance, created = Movie.objects.get_or_create(imdb_id=movie_instance.imdb_id)
                # if created:
                # TODO: add a check to make sure duplicates are not saved to db

                # movie_instance.save()
                # print("movie_instance.imdb_id-------------",movie_instance.imdb_id)
                # if created:
                #     movie.save()

    return render(request, 'success.html')



genre_choices = [
    "War",
    "Animation",
    "Biography",
    "Adventure",
    "Sport",
    "Crime",
    "Action",
    "Romance",
    "Fantasy",
    "Documentary",
    "Music",
    "Horror",
    "Mystery",
    "Comedy",
    "Drama",
    "Family",
    "Thriller",
    "Sci-Fi",
    "History"]


class MovieListView(SingleTableView, FilterView):
    model = Movie
    table_class = MovieTable
    template_name = 'movie_list.html'
    paginate_by = 10
    filterset_class = MovieFilter

    def get_queryset(self):
        queryset = super().get_queryset()

        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        genre_filter = self.request.GET.getlist('genre')  # Use getlist to get multiple values for genre
        if genre_filter:
            for genre in genre_filter:
                queryset = queryset.filter(genre__contains=[genre])

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        unique_genres = genre_choices
        print('unique_genres--------------', unique_genres)
        context['genre_choices'] = unique_genres
        print('context', context['genre_choices'])
        return context
