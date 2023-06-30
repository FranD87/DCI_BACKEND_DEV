
from django.urls import path
from website.views import home, Profile, login, create_user, Base, Main, product_list
app_name = 'website'

urlpatterns = [
   path('', home, name='home'),
   path('profile/', Profile.as_view(), name='user-profile'),
   path('login/', login, name='login'),
   path('usercreate/', create_user, name='create-user'),
   path('browse/',Base.as_view(), name='browse'),
   path('main/', Main.as_view(), name='main'),
   path('products/', product_list, name='product-list')

]