# -*- coding: utf-8 -*-
from django.shortcuts import render
#bring in the HttpResponse
from django.http import HttpResponse

# Create your views here.

# when index is loaded give us the request object
def index(request):
    return HttpResponse('Hello Wolrd')
