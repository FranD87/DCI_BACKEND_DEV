


class CustomHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['FRAN_custom_header'] = 'MY CUSTOM HEADER'
        return response

    def process_response(self, request, response):
        return response

'''
Middleware in Django is a component that sits between the web server and the view functions or other middleware. It 
plays a crucial role in the request/response processing pipeline. Each middleware component can inspect, modify, or 
take action on requests and responses. It provides a way to perform common operations or implement cross-cutting 
concerns for multiple views in a centralized and reusable manner.

Middleware can perform various tasks, such as:
- Processing and modifying request headers or parameters.
- Authenticating or authorizing requests.
- Handling sessions and cookies.
- Performing URL rewriting or redirection.
- Compressing or decompressing content.
- Caching responses.
- Logging or monitoring requests.
- Injecting additional information or context into requests or responses.

Middleware operates in a chain, where each middleware component receives the request in the order defined in the 
Django settings. It can optionally modify the request or perform some processing before passing it on to the next 
middleware in the chain. Similarly, middleware can intercept the response and modify it before it reaches the client.

By leveraging middleware, you can implement reusable and centralized logic that is applied to requests and responses 
across multiple views, providing a way to handle cross-cutting concerns and keep your codebase clean and modular.

Class: CustomHeaderMiddleware
- Defines the `__init__` method that initializes the middleware with a `get_response` parameter.
- Defines the `__call__` method, which is called for each request.
  - Receives a `request` object.
  - Calls the `get_response` function with the `request` object and assigns the response to the `response` variable.
  - Sets a custom header `'FRAN_custom_header'` in the response with the value `'MY CUSTOM HEADER'`.
  - Returns the modified `response` object.
- Defines the `process_response` method.
  - Receives the `request` and `response` objects.
  - Returns the `response` object.

The string `'session_project.custom_middleware.CustomHeaderMiddleware'` refers to the fully-qualified name of the 
`CustomHeaderMiddleware` class in the `session_project` Django project, specifically in the `custom_middleware` module.

To use this middleware in your Django project, you need to follow these steps:

1. In your Django project, locate the settings module (usually named `settings.py`).
2. In the `MIDDLEWARE` setting, add the string `'session_project.custom_middleware.CustomHeaderMiddleware'` to 
   the list of middleware classes.
   - Example: `MIDDLEWARE = [ ..., 'session_project.custom_middleware.CustomHeaderMiddleware', ... ]`
3. Save the changes to the settings module.

By adding the middleware class to the `MIDDLEWARE` setting, Django will include it in the middleware stack and execute 
its `__call__` method for each incoming request, allowing you to modify the response by adding a custom header.
'''