from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(*args, **kwargs): # *args, **kwargs are just python things, they are used to be able to pass any number of arguments into the function. *args becomes a tuple, it is not mutable but we can iterate through it.
    #**kwargs is similiar but it takes a number of key, value pairs s.a a="Real", b="Python", c="Is", d="Great".
    # we can iterate with f.ex for arg in kwargs.values(): or for arg in kwargs: (to iterate through keys)
    # The correct order for your parameters is:
        # 1. Standard arguments
        # 2. *args arguments
        # 3. **kwargs arguments
    # Note: we can change *args to *anyname and similiar to kwargs
    # We can use the unpack operator * to turn list objeccts into tuples of 
    # the values instead.
    return HttpResponse("<h1>Hello World</h1>") # IH: HttpResponse takes the string and turns it into html code

def contact_view(request, *args, **kwargs):
    # IH: the request parameter is optional
    # It can be smart to print out the request for debugging
    # We can also retrieve a lot of things like requet.user and request.path (called template tags)
    return render(request, "contact.html", {}) # IH: we are rendering an html template, the code inside the template is not necessarily pure html.
    # See templates in the root folders templates/
    # Note how we are using template inheritance with base.html as a base class
    # and then contact.html fills in some blocks with {% block content %}

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "this is about us",
        "my_number": 123,
        "my_list": ["a", "b", "c", 22],
    }
    # IH: with the third parameter, we can send in a context (a dict)
    # which can be used inside the html template. 
    # See about.html where we get the values by refering to the keys that we expect
    return render(request, "about.html", my_context)  


# IH: prefarably   we perform most of the logic in the views and only small parts of iterating and
# logical statements in the html templates.