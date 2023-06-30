from django.urls import path
from . views import main, home, login, test_view

app_name = 'session_app'

urlpatterns = [

    path('', main, name='main'),
    path('home/', home, name='home'),
    path('login/', login, name='login'),
    path('test/', test_view, name='test')
]