# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView #Get the generic view
from .models import *

class HomePageView(ListView): # Name of classes should always be capitalize unlike functions
    model= Quote
    template_name = 'home.html'
    context_object_name = 'quotes_list'