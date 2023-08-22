from django.shortcuts import render
from django.http import HttpResponse

# for trying out debugging
def calculate():
    x = 1
    y = 2
    return x

# Create your views here.
def say_hello(request):
    # return an instance of the HttpResponse class
    # arguments of HttpResponse are objects - can be a string for example
    # now we need to map a url to this view -> make a urls.py file and open
    # return HttpResponse('hello world')

    # now try returning an HTML template
    # at first returned error because I did not put the html file in a 'templates' folder
    # return render(request, 'hello.html')

    # now try adding some dynamic value
    # the next argument can be any mapping from string to object - try dictionary
    # return render(request, 'hello.html', {'name': 'Adam'})

    # now debugging - add breakpoint and run debug - remove when done
    x = calculate()
    return render(request, 'hello.html')