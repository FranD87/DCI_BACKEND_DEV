"""
URL configuration for hello project.

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
from django.urls import path, re_path
# from shop.views import home, product_by_id, product_view
from shop.views import home, products_view,product_by_id, product_test, song_by_month, student_list, main, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('product/<int:item_id>', product_by_id),
    path('products', products_view),
    path('product/<str:test>', product_test),
    path('song/<int:month>', song_by_month, {'is_int': True}),
    path('song/<str:month>', song_by_month, {'is_int': False}),
    path('student_list/', student_list, name='students'),
    path('main/', main, name='main'),
    path('login/', login, name='login')

]