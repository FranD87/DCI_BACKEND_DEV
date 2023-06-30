from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect, Http404

# Create your views here.
def home(request):
    http_string: str = "blog home page"
    return HttpResponse(http_string)

def redirect(request):
    redirect_to = reverse_lazy("blog:home")
    return HttpResponseRedirect(redirect_to)

def bad_request_view(request):
    http_string: str = "blog bad request"
    return Http404(http_string)

def create_page(request):
    http_string: str = "blog create page"
    return HttpResponse(http_string)