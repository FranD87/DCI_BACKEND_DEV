from django.urls import path
from .views import home, redirect, bad_request_view, create_page



app_name = "blog"

urlpatterns = [
    path("", home, name="home"),
    path("redirect/", redirect, name="redirect"),
    path("bad_request/", bad_request_view, name="bad_request"),
    path("create_page/", create_page, name="create_page")
]