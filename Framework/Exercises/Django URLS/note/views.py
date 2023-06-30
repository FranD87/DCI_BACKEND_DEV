from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    '''Some logic of landing page'''
    return HttpResponse('Welcome to my course notes!')

def sections(request):

    response = [
        "<h1>Browse my notes by section</h1>",
        "<ol>",
        "<li>Web Frameworks</li>",
        "<li>Setting up Django</li>",
        "<li>URL Mapping</li>",
        "</ol>",
        '<a href="http://127.0.0.1:8000/">Back to home</a>'
    ]
    return HttpResponse(''.join(response))

def section_by_name(request, section_name):
    if section_name == 'frameworks':
        result = ["<h1>Some header for Framework section</h1>",
                  "<ol>",
                  "<li>Some info 1</li>",
                  "<li>Some info 2</li>",
                  "<li>Some info 3</li>",
                  "</ol>",
                  '<a href="http://127.0.0.1:8000/sections">Back to sections</a>'
                  ]
    elif section_name == 'Setting up Django':
        result = ["<h1>Some header for Set Up Django section</h1>",
                  "<ol>",
                  "<li>Some info 1</li>",
                  "<li>Some info 2</li>",
                  "<li>Some info 3</li>",
                  "</ol>",
                  '<a href="http://127.0.0.1:8000/sections">Back to sections</a>'
                  ]
    else:
        if section_name == 'URL Mapping':
            result = ["<h1>Some header for Set Up Django section</h1>",
                  "<ol>",
                  "<li>Some info 1</li>",
                  "<li>Some info 2</li>",
                  "<li>Some info 3</li>",
                  "</ol>",
                  '<a href="http://127.0.0.1:8000/sections">Back to sections</a>'
                  ]

    return HttpResponse(''.join(result))

def sections(request):

    response = [
        "<h1>Browse my notes by section</h1>",
        "<ol>",
        '<li><a href="http://127.0.0.1:8000/section/frameworks">Web Frameworks</a></li>',
        "<li>Setting up Django</li>",
        "<li>URL Mapping</li>",
        "</ol>",
        '<a href="http://127.0.0.1:8000/">Back to home</a>'
    ]
    return HttpResponse(''.join(response))
