from django.urls import path
from ..views.feedback import home, feedback_redirect, FeedbackCreateView, FeedbackUpdateView


app_name = 'feedback'
urlpatterns = [
    path('', home, name='home'),
    path('<int:feedback_id>/update', FeedbackUpdateView.as_view(), name="update_feedback"),
    path('redirect/', feedback_redirect, name='redirect'),
    path("add/", FeedbackCreateView.as_view(), name='create_feedback'),
]
