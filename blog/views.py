from django.shortcuts import render
from django.http.response import HttpResponse


def blog_app(request):
    return HttpResponse("first app with django")
