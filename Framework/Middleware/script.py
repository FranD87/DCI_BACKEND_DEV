
# Lets create and test our own middleware
# start new django project
# create view:
# def main(request):
#     return HttpResponse('Hello World')
# create url for it:
# path('', main, name='main')
# test it with postman and check the headers
# lets create file in project folder middleware.py
# class CustomHeaderMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         response = self.get_response(request)
#         response['Custom-Header'] = 'MY CUSTOM HEADER'
#         return response
#
#     def process_response(self, request, response): -> this is build method to process and return created response
#         return response
# We can create our own Middleware using closures. The main point here is the function returned. This function takes a
# request and returns a response, just like any view, but one peculiarity happens inside the function, it calls the
# closure argument (get_response) to get the response. Before calling this function only the request object is
# available and we can change it as we like. After the function is called we also have the response object available.
# Outside the middleware function we can define any setup that needs to run on initialisation.
# add our custom middleware to settings.py:
#     'my_project.middleware.CustomHeaderMiddleware',
# test it with postman
# here is documentation about middleware:
# https://docs.djangoproject.com/en/4.2/topics/http/middleware/



