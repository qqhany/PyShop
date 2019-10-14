from django.http import HttpResponse
# / products -> index
# Uniform Resource Locator (address)


def index(request):
    return HttpResponse('Hello World')


def new(request):
    return HttpResponse('New products')