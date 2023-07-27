from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from django_tables2 import SingleTableView

from django_filters.views import FilterView
from .models import Movie
from .tables import MovieTable
import requests
import json
from django.shortcuts import render
from .models import Movie

import json
import django_filters
from django.shortcuts import render
from .models import Movie
# from .tables import MovieTable, MovieFilter
from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Movie
from .tables import MovieTable

import requests
from django.shortcuts import render
from .models import Movie
from .tables import MovieTable
from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Movie
from .tables import MovieTable
from .filters import MovieFilter
from django.db.models import Count

from django.shortcuts import redirect

def clear_filters(request):
    return redirect('movies-list')

def fetch_and_save_movies(request):
    # Replace 'YOUR_URL_HERE' with the actual URL containing the JSON data
    url = 'http://127.0.0.1:3000/movies'

    # Fetch data from the URL
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


#
# def movies_table_view(request):
#     # Replace 'your_data_url' with the actual URL that returns the movie data
#     queryset = Movie.objects.all()
#
#     # Create a MovieFilter instance and apply it to the queryset
#     movie_filter = MovieFilter(request.GET, queryset=queryset)
#     queryset = movie_filter.qs
#
#     # Create a MovieTable instance and pass the filtered queryset
#     table = MovieTable(queryset)
#
#     return render(request, 'movies_table.html', {'table': table, 'movie_filter': movie_filter})

#
# def movie_list(request):
#     table = MovieTable(Movie.objects.all())
#     filter = MovieFilter(request.GET, queryset=Movie.objects.all())
#     table = MovieTable(filter.qs)
#
#     RequestConfig(request, paginate={'per_page': 10}).configure(table)
#
#     return render(request, 'movie_list.html', {'table': table, 'filter': filter})

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
            # For each selected genre, use contains lookup to search within the array
            for genre in genre_filter:
                queryset = queryset.filter(genre__contains=[genre])

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get unique genre choices from the queryset
        # unique_genres = Movie.objects.values_list('genre', flat=True).distinct()
        unique_genres = genre_choices
        print('unique_genres--------------', unique_genres)
        context['genre_choices'] = unique_genres
        print('context', context['genre_choices'])
        return context

# "title", "date", "year", "rated", "released", "runtime", "genre", "director", "writer", "actors", "plot", "language", "country", "awards", "poster", "meta_score", "imdb_rating", "imdb_votes", "imdb_id", "type", "dvd", "box_office", "production", "website",
# Filter functionality
# genre_filter = self.request.GET.get('genre')
# # genre_filter = self.request.GET.get('released')
# # genre_filter = self.request.GET.get('year')
# # genre_filter = self.request.GET.get('runtime')
# # genre_filter = self.request.GET.get('director')
# # genre_filter = self.request.GET.get('writer')
# # genre_filter = self.request.GET.get('actors')
# # genre_filter = self.request.GET.get('genre')
# # print("trying to filter",genre_filter)
# if genre_filter:
#     queryset = queryset.filter(genre__icontains=genre_filter).order_by('title')
# filter = MovieFilter(self.request.GET, queryset=queryset)
# queryset = filter.qs
# return queryset
