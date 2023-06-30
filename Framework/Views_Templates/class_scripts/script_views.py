
# start new project and create website view:
# def website(request):
#     user = request.GET['user']  # -> we will get key error if user not provided
#     user = request.GET.get('user')
#     if not user:
#         return HttpResponse('please provide user')
#     return HttpResponse('Hi Julia')'
# test it with urls
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/?user=julia

# add next lines to code:
# user = request.user
#     print(user)
#     print(user.id)
# test it with login to admin and without

# test it with views
# def welcome(request):
#     user = request.user
#     response = HttpResponse()
#     if user.is_authenticated:
#         response.write(f'Hello {user}')
#     else:
#         response.write('Hello AnonymousUser')
#     return response
# HttpResponseRedirect
# The HttpResponseRedirect returns a response that triggers a redirection to the indicated path (in this case, the
# home of the website).
# create function in views:
# def profile(request):
#     if request.user.is_authenticated:
#         return HttpResponse('Hello')
#     else:
#         return HttpResponseRedirect('/')
# test it with admin when you are loged in or no

# from django.views.decorators.http import require_http_methods
# decorate created functions
# POST method is used when we are interacting with user or other server and updating or adding some
# information to our DB
# render function:

# Class Based Views:
# There is a method for each HTTP method: get, post, delete. The class will call each function depending on the
# request method.
# We need to call the method as_view() of the View extending class.
# views.py:
# class Profile(View):
#     massage = 'Hello AnonymousUser'
#     def get(self, request):
#         if request.user.is_authenticated:
#             self.massage = f'Hello {request.user}'
#         return HttpResponse(self.massage)
# urls.py:
# path('user_profile', Profile.as_view(), name='user_profile')

# introduce postman
# snap install postman
# create function in views:
# @require_http_methods(['GET'])
# def login(self, request):
#         massage = 'Hello anonim user'
#         if 'username' in request.GET and 'password' in request.GET:
#             self.massage = f'Hello {request.GET.get("username")}'
#         return HttpResponse(massage)
# @csrf_exempt
# @require_http_methods(['POST', 'PUT', 'DELETE'])
# def create_user(request, id):
#         user = {}
#         user['username'] = request.POST.get('username')
#         print(request.POST)
#         user['email'] = request.POST.get('email')
#         user['password'] = request.POST.get('password')
#         # save toDB new user
#         return JsonResponse(user)
# test it with postman and urls
# http://127.0.0.1:8000/user_profile



