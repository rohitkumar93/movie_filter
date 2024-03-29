"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from movies.views import *

router = DefaultRouter()
router.register(r'movie', MovieViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('admin/', admin.site.urls),
    # path("movies/", movie_list),
    path('movies-list/', MovieListView.as_view(), name='movies-list'),
    path('fetch-and-save-movies/', fetch_and_save_movies, name='fetch_and_save_movies'),
    path('clear-filters/', clear_filters, name='clear-filters'),
]
