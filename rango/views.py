from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    # Request the context of the request.
    # The context contains info such as the client browser, etc.
    context = RequestContext(request)
    
    # Construct a dictionary to pass to the template engine.
    # Note the key boldmessage is the same as {{ boldmessage }}
    context_dict = {'boldmessage': "I am bold font from the context var in views.py."}
    
    # Return a rendered reponse to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we want to use.
    return render_to_response('rango/index.html', context_dict, context)
    
    
def about(request):
    context = RequestContext(request)
    
    return render_to_response('rango/about.html', context)
