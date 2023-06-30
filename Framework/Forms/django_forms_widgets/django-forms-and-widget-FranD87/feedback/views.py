from typing import Any, Dict
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.views.generic.edit import FormView 
from django.views.generic.base import TemplateView
from .forms import FeedbackDataForm, FeedbackDataModelForm



def home(request: WSGIRequest) -> HttpResponse:
    html_value: str = '''
    <h1> Response</h1>
    <p> Feedback form Successfully Submitted </p>
    '''
    return HttpResponse(html_value)

class FeedbackDetailsView(FormView):
    form_class = FeedbackDataModelForm
    template_name = 'feedback/feedback_form.html'
    #success_url = reverse_lazy('feedback:home')
    def get_success_url(self):
        # any other customizations here
        return reverse_lazy('feedback:home')

