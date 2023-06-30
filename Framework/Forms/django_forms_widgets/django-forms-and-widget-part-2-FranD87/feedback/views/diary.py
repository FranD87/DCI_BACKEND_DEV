from typing import Any, Dict
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from django.template.response import TemplateResponse
from django.core.handlers.wsgi import WSGIRequest
from django.views.generic.edit import FormView


def home(request: WSGIRequest) -> HttpResponse:
    return TemplateResponse(request, 'diary/home.html', {})


def diary_redirect(request: WSGIRequest) -> HttpResponse:
    return TemplateResponse(request, 'diary/redirect.html', {})
