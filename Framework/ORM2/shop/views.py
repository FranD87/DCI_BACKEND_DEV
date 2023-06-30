from django.shortcuts import render
from django.http import HttpResponse
from shop.models.test import Test
from shop.models.user import User
from shop.models.post import Post
from shop.models.students import Students
from shop.models.school_classes import Class

# Create your views here.
def main(request):
    return HttpResponse('Hello')

def test(request):
    item_key_val = Test.objects.filter(json__my_key='test string')
    print(item_key_val.values)
    item_key = Test.objects.filter(json__has_key='my_key')
    print(item_key)
    return HttpResponse('test view')


def user_post(request):
    my_user, status = User.objects.get_or_create(email='test2@gmail.com', password='ABC')
    # post = Post.objects.create(user=my_user, title='Post related title', post='Some text')
    # post1 = Post.objects.create(user_id=2, title='post 2', post='Some info fro post 2')
    # posts = Post.objects.filter(user=my_user)
    # print(posts)
    # post = my_user.post_set.create(title='test 3 title', post='some post')
    # post1 = Post.objects.create(title='test no user 1', post='Some post')
    # post2 = Post.objects.create(title='Test 2 no user', post='some other post')'
    # print(Post.objects.filter(user=my_user))
    # post1 = Post.objects.get(id=7)
    # post2 = Post.objects.get(id=6)
    # my_user.post_set.add(post1, post2)
    # my_user.post_set.remove(post1)
    # print(Post.objects.filter(user=my_user))
    print(my_user.post_set.filter(title__startswith='t'))
    return HttpResponse('User created')

def student_classes(request):
    student1 = Students.objects.get(id=1)
    student2 = Students.objects.get(id=2)
    django_class = Class.objects.create(title='django class', info='some test text')
    english_class = Class.objects.create(title='english class', info='some est info')
    django_class.student.add(student1, student2)
    english_class.student.add(student1)
    return HttpResponse('Here is some students')
