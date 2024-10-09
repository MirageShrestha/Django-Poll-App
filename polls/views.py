from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, Mirage. You are at the polls index')