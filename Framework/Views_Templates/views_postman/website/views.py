from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.views.generic import TemplateView
from website.objects.user import User

# Create your views here.
def home(request):
    response = HttpResponse()
    user = request.user
    if user.is_authenticated:
        response.write(f'Hello {user}')
        return response
    else:
        return HttpResponseRedirect('admin/')

class Profile(View):

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponse(f"Hello {request.user}")
        else:
            return HttpResponse("Hello Anonymous")

@require_http_methods(['GET'])
def login(request):
    if request.user.is_authenticated:
        return HttpResponse(f'Hello {request.user}')
    else:
        return HttpResponse('Hello Anonymous')

@csrf_exempt
@require_http_methods(['POST'])
def create_user(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    # EG: if 'username' in request.POST and 'email' in request.POST:
    # Here will be some process of checkin and creating new user in DB
    user = {'username': username, 'password': password, 'email': email}
    return JsonResponse(user)

class Base(View):
    def get(self, request):
        template = get_template('website/browse_home.html')
        context = {'my_var': 'Hello World!'}
        return HttpResponse(template.render(context))

class Main(TemplateView):
    template_name = "website/browse_home.html"
    def get_context_data(self, **kwargs):
        context = {'my_var': 'Hello User', 'my_list': [1, 5, 7], 'my_dict': {'user_name': 'Fran'}, 'user': User()}
        return context

def product_list(request):
    context = {'products': [{'name': 'laptop', 'quantity': 3,}, {'name': 'tablet', 'quantity': 10}]}
    return render(request, 'website/product_list.html', context)




