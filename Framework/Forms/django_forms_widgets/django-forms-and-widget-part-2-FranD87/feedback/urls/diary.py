from django.urls import path
from ..views.diary import home, diary_redirect


app_name = 'diary'
urlpatterns = [
    path('', home, name='home'),
    # path("<int:diary_id>/update", add_class_view, name="diary-update"),
    # path("add/", add_class_view, name="diary-add"),
    path('redirect/', diary_redirect, name='redirect')
]
