from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'register.html')


def save_user(request):
    dict1 = request.GET
    name = dict1['name']
    email = dict1['email']
    mobile = dict1['mobile']
    return HttpResponse(f'{name}, {email}, {mobile} collected')

