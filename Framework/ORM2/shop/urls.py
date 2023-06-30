from django.urls import path
from shop.views import main, test, user_post, student_classes

app_name = 'shop'
urlpatterns = [
    path('', main, name='main'),
    path('test/', test, name='test'),
    path('post/', user_post, name='user_post'),
    path('student/', student_classes, name='student') 
]

