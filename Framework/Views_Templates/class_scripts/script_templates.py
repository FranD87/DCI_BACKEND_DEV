# Templates

# create function in views:
# class Base(View):
#     def get(self, request):
#         template = get_template("browse_home.html")  -> will search for file in templates folder and return str with HTML code
#         context = {"my_variable_name": "Hello World!"}
#         return HttpResponse(template.render(context))
# Create templates folder
# create file there browse_home.html
# <html>
# <head>
#   <title>Browse the shop!</title>
# </head>
# <body>
#   <h1>{{ my_variable_name }}</h1>
# </body>
# </html>
# add to urls:
# path('base/', Base.as_view(), name='base')
# TemplateView example
# class Main(TemplateView):
#     template_name = 'website.html'
#     def get_context_data(self, **kwargs): -> all url params go as kwargs args
#         return {'data': 'hello world'}
# urls:
# path('website/', Main.as_view(), name='website')
# To avoid naming conflicts, it is common practice to put the html file in a directory with the same name as the app.
# create folder website in templates and place there main.html
# template_name = 'website/main.html'

# change main.html:
# <html>
# <head>
#   <title>Main</title>
# </head>
# <body>
#   <h1>{{ data }}</h1>
#   <p>{{ list }}</p>
# </body>
# </html>
# add list var to context
# return {'data': 'hello world', 'list': ['a', 'b', 'c']}
# The dot (.) can be used to access elements in lists and dictionaries.
# views:
# return {'data': 'hello world', 'list': ['a', 'b', 'c'], 'dict': {'user_name': 'Julia'}}
# html:
#   <p>{{ list.1 }}</p>
#   <h2>{{ dict.user_name }}</h2>
# The dot (.) can also be used to access object properties and methods.
# create objects folder and user.py file
# class User:
#     name = 'Maria'
#     def get(self):
#         return 37
# pass it as context to view:
# return {'data': 'hello world', 'list': ['a', 'b', 'c'], 'dict': {'user_name': 'Julia'}, 'object': User()}
# add it as output in main.html
#   <h3>{{ object.name }}</h3>
#  <h3>{{ object.get }}</h3> -> Note that using object methods does not require parenthesis (actually it requires us
#  to NOT use them).
# Since all data types in Python are objects, this means we can also access the methods of the built-in data types to
# do all sorts of things.
# {% for word in text.split %}
#       <li>{{ word }}</li>
#  {% endfor %}
# Django template language have a lot of filters. Filters can be used to modify the output of a variable.
# <h3>{{ object.get|add:3 }}</h3>

# Template tags are wrapped in {% %}
# if and for are template tags.
#   <ul>
#     {% if list %}
#       {% for item in list %}
#             <li>{{ item }}</li>
#       {% endfor %}
#     {% else %}
#       <li>No items found.</li>
#     {% endif %}
#   </ul>
# test it with empty and normal list
# The for tag allows for an empty clause that catches an empty list.
# <ul>
#     {% for item in items %}
#       <li>{{ item }}</li>
#     {% empty %}
#       <li>No items found.</li>
#     {% endfor %}
#   </ul>
# The comment tag allows us to comment code in a clean way.
# {% comment "Some internal note" %}
#   <p>This will not be printed.</p>
# {% endcomment %}
# The url tag returns the URL matching the named path.
# add to main.html:
# <a href="{% url 'welcome' %}">Home</a>
# Template Inheritance
# create layout.html:
# <html>
#   <head><title>{% block title %}{% endblock %}</title></head>
#   <body>
#     <p>Page header, Menu etc</p>
#     {% block page-content %}
#     {% endblock %}
#     <p>Footer, contacts, etc</p>
#   </body>
# </html>
# create product_list.html
# {% extends 'layout.html' %}
# {% block page-content %}
#   <h1>Welcome to the shop!</h1>
#   <p>Here is out product list</p>
#   <ul>
#         {% for item in products %}
#               <li>{{ item.name }}</li>
#         {% endfor %}
#     </ul>
# {% endblock %}
# create view:
# def product_list(request):
#     products ={'products': [{'name': 'laptop', 'quantity': 3}, {'name': 'tablet', 'quantity': 10}]}
#     return render(request, 'product_list.html', products)
# urls:
# path('product_list/', product_list, name='product-list')
# Static files in Django

# create dir static
# create dur css inside static
# create file main.css
# body{
# background-color: red;
# }
# add to layout:
# {% load static %}
# add to layout header:
# <link href="{% static 'css/main.css' %}" type="text/css" rel="stylesheet">
# test website



