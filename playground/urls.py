# this module maps urls to view functions 
from django.urls import path
from . import views

# URLConf module (URL configuration)
# it is important that this variable is spelled this way
urlpatterns = [
    #path('playground/hello/', views.say_hello) # note we are not calling the function say_hello, just passing a reference to it
    path('hello/', views.say_hello) # don't need to have 'playground/' any more since we reference this module in the main urls.py
]

# each app can have their own URL configuration, but you need to pass it into the main URL config file for the project
# in this case that's barnacle