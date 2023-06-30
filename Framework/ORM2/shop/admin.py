from django.contrib import admin
from shop.models.city import City
from shop.models.photo import Photo
from shop.models.logo import Logo
from shop.models.test import Test
from shop.models.user import User
from shop.models.post import Post
from shop.models.test_post import TestPost
from shop.models.user_profile import UserProfile
from shop.models.students import Students
from shop.models.school_classes import Class

# Register your models here.
admin.site.register(Class)
admin.site.register(Students)
admin.site.register(City)
admin.site.register(Photo)
admin.site.register(Logo)
admin.site.register(Test)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(TestPost)
admin.site.register(UserProfile)
