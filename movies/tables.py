import django_tables2 as tables
from django.shortcuts import render

from .models import Movie

class MovieTable(tables.Table):
    class Meta:
        model = Movie
        # template_name = "django_tables2/bootstrap.html"
        template_name = "django_tables2/bootstrap5-responsive.html"
        fields = ("title", "poster", "genre", "released", "meta_score", "runtime")
        empty_text = ("No movies match your query")

    def movie_list(request):
        # Your view logic here to get queryset and other filters if any
        queryset = Movie.objects.all()
        table = MovieTable(queryset)

        context = {
            "table": table,
        }

        return render(request, "movie_list.html", context)
