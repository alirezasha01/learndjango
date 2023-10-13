from django.http.response import HttpResponse

def home_page(request):
    return HttpResponse("hello world")