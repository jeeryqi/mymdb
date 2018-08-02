from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Movie, Person


# Create your views here.

class MovieList(ListView):
    model = Movie
    paginate_by = 3


class MovieDetail(DetailView):
    queryset = Movie.objects.all_with_related_persons()

class PersonDetail(DetailView):
    queryset = Person.objects.all_with_prefetch_movies()