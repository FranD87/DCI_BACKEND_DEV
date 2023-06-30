from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
def home(request):
    '''Some logic of lending page'''
    return HttpResponse('Hello Frank')

def products_view(request):
    '''Some logic for product list'''
    return HttpResponse('Here is a list of all products')

def product_by_id(request, item_id):
    '''Retrieve item from DB by ID'''
    return HttpResponse(f'Here is details of product with id: {item_id}')

def product_test(request, test):
    return HttpResponse('Here we are making testing')

def song_by_month(request, month, is_int):
    if is_int:
        return HttpResponse('Month is digit')
    return HttpResponse('Month is string')

def student_list(request):
    response = [
        '<h1>Students list</h1>',
        '<ol>',
        '<li>Frank</li>',
        '<li>BOB</>',
        '<li>Harry</>',
        '</ol>',
        '<a href="',
        reverse('home'),
        '">Back to home</a>'

    ]
    return HttpResponse(''.join(response))

def main(request):
    if 'username' in request.GET and 'password' in request.GET:
        username = request.GET['username']
        return HttpResponse(f'Welecome {username}')
    return redirect('login')

def login(request):
    return HttpResponse('Please login')
