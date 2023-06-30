from django.urls import path
from .views import home, FeedbackDetailsView


app_name = 'feedback'
urlpatterns = [
    path('', home, name='home'),
    path('detail/', FeedbackDetailsView.as_view(), name='feedback_detail')
]
