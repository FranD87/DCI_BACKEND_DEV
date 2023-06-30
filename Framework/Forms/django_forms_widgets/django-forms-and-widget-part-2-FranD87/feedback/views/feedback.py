from typing import Any, Dict
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from django.template.response import TemplateResponse
from django.core.handlers.wsgi import WSGIRequest
from django.views.generic.edit import FormView

from ..models import Feedback
from ..forms import FeedbackDataForm, FeedbackDataModelForm


def home(request: WSGIRequest) -> HttpResponse:
    feedbacks = Feedback.objects.all()
    return TemplateResponse(request, 'feedback/home.html', {"feedbacks": feedbacks})


def feedback_redirect(request: WSGIRequest) -> HttpResponse:
    return TemplateResponse(request, 'feedback/redirect.html', {})



class FeedbackCreateView(FormView):
    form_class = FeedbackDataForm
    template_name = 'feedback/feedback_form.html'
    #success_url = reverse_lazy('feedback:home')

    def get_success_url(self):
        # any other customizations here
        return reverse_lazy('feedback:home')

    # Override the get method in for views
    # def get(self, request, *args, **kwargs):
    #     #data: dict {"name"}: "John Doe", "email": "john@test.com"
    #     #bound_form = self.form_class(data)
    #     form_item = FeedbackDataForm()
    #     #form_item = self.form_class() '''Unbound form class'''
    #     context: dict = {"form": form_item}# add bound_form into value to interpret bound_form action.
    #     # It bounds info to the fields
    #     return TemplateResponse(request, self.template_name, context)

    # Override the POST method
    def post(self, request, *args, **kwargs) -> HttpResponse:
        form_data = self.get_form()
        for item in form_data:
            print(item.name, " : ", item.value())
        #print(request.POST)# Holds all the info contained in the form
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        email: str = form.cleaned_data.get('email')
        if 'test' in email:
            form.add_error('email', "Invalid email address")
            return super().form_valid(form)
        Feedback.objects.create(**form.cleaned_data)


class FeedbackUpdateView(FormView):
    form_class = FeedbackDataForm
    template_name = 'feedback/home.html'

    def get_success_url(self) -> str:
        return reverse_lazy('feedback:home')


    def get(self, request, *args, **kwargs):
        print(kwargs, " ", self.kwargs) # Url information
        feedback_id = self.kwargs.get('feedback_id')
        feedback_record = Feedback.objects.filter(id=feedback_id)
        feedback_data: dict = feedback_record.values()[0]
        unbound_form = self.form_class()
        bound_form = self.form_class(feedback_data)
        context: dict = {"form": unbound_form}
        return TemplateResponse(request, self.template_name, context)

    def form_valid(self, form):
        feedback_id = self.kwargs.get("feedback_id")
        feedback_item = Feedback.objects.filter(id=feedback_id)
        feedback_item.update(**form.cleaned_data)
        return super().form_valid(form)


'''
Method: home(request: WSGIRequest) -> HttpResponse:
- Retrieves all Feedback objects from the database.
- Renders the 'home.html' template with the retrieved feedbacks as a context variable.

Method: feedback_redirect(request: WSGIRequest) -> HttpResponse:
- Renders the 'redirect.html' template.

Class: FeedbackCreateView(FormView):
- Specifies the form class as `FeedbackDataForm`.
- Sets the template name to 'feedback/feedback_form.html'.
- Defines a `get_success_url()` method that returns the URL for redirecting after a successful form submission.
- Overrides the `post()` method to handle form submission.
  - Retrieves the form data.
  - Prints the name and value of each form field.
  - Calls the parent `post()` method to handle the form submission.
- Implements the `form_valid()` method to handle valid form submissions.
  - Retrieves the email from the form's cleaned data.
  - Checks if the email contains the word 'test'.
  - If 'test' is found in the email, adds an error to the email field and returns the form.
  - If the email is valid, creates a new Feedback object using the form's cleaned data.


Class: FeedbackUpdateView(FormView)
- Specifies the form class as `FeedbackDataForm`.
- Sets the template name to 'feedback/home.html'.
- Defines a `get_success_url()` method that returns the URL for redirecting after a successful form submission.
- Overrides the `get()` method to handle GET requests.
  - Retrieves the `feedback_id` from the URL keyword arguments (`kwargs`).
  - Filters the `Feedback` objects based on the `feedback_id`.
  - Retrieves the data of the first `Feedback` object as a dictionary.
  - Initializes an unbound form instance (`unbound_form`) using `FeedbackDataForm`.
  - Initializes a bound form instance (`bound_form`) using `FeedbackDataForm` and the retrieved `feedback_data`.
  - Creates a context dictionary with the unbound form as the value for the key "form".
  - Renders the template 'feedback/home.html' with the provided context.
- Overrides the `form_valid()` method to handle valid form submissions.
  - Retrieves the `feedback_id` from the URL keyword arguments.
  - Filters the `Feedback` objects based on the `feedback_id`.
  - Updates the retrieved `feedback_item` with the cleaned data from the form.
  - Calls the parent `form_valid()` method to handle the form submission.

This class represents a view for updating a `Feedback` object. It displays a form pre-filled with the existing 
feedback data and allows the user to update and submit the form. Upon successful submission, the `Feedback` object is 
updated with the new data.
'''




