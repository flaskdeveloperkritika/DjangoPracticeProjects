from django.http import HttpResponse


def say_hello_world(request):
    return HttpResponse('Hello World')


def say_bye(request):
    return HttpResponse('Bye')


def say_welcome(request):
    return HttpResponse('<h1>Hello user Welcome to my website</h1>')