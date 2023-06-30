from django.shortcuts import render
from django.http import HttpResponse
from movie.models import Movie
# Create your views here.


def main(request):
    item = Movie.objects.filter(name='title')
    return HttpResponse(f'Movies: {item}')