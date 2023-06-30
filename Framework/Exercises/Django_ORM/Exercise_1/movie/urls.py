from django.contrib import admin
from django.urls import path
from movie.views import main
app_name = 'movie'


urlpatterns = [
    path('', main, name='main'),

]