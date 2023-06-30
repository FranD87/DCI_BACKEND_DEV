from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.

def main(request):
    request.session.set_expiry(60)
    message = json.dumps(request.COOKIES)
    session_id = request.session.session_key
    print('Expires on', request.session.get_expiry_date())
    print('Expires in', request.session.get_expiry_age())
    print(session_id)
    #request.session.flush()# -> Remove session
    #request.session.clear_expired()# -> clean all expired session information
    return HttpResponse(message)

def home(request):
    user_id = request.session.get('my_user_id')
    if user_id is not None:
        user = User.objects.get(pk=user_id)
        return render(request, 'session_app/home.html', {'user': user})
    else:
        return redirect('session_app:login')

def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            request.session['my_user_id'] = user.id
            return redirect('session_app:home')
    return render(request, 'session_app/login.html')

def test_view(request):
    return HttpResponse('Hello world')

'''
Method: main(request)
- Imports necessary modules and classes.
- Receives a `request` object.
- Sets the session expiry time to 60 seconds.
- Converts the `request.COOKIES` dictionary into a JSON string and assigns it to the `message` variable.
- Retrieves the session ID using `request.session.session_key` and assigns it to the `session_id` variable.
- Prints the expiry date and expiry age of the session.
- Prints the session ID.
- Returns an HTTP response with the `message` as the content.


Method: home(request)
- Retrieves the user ID from the session.
- If the user ID exists:
- Retrieves the User object corresponding to the user ID.
- Renders the 'home.html' template with the user object as a context variable.
- If the user ID doesn't exist:
- Redirects the user to the 'login' URL.

Method: login(request)
- Checks if the request method is POST.
- If the request method is POST:
- Authenticates the user using the provided username and password.
- If the authentication is successful:
- Stores the user ID in the session under the key 'my_user_id'.
- Redirects the user to the 'home' URL.
- Renders the 'login.html' template if the request method is not POST or if the authentication fails.
'''

