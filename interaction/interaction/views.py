from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'home.html')


def interact(request):
    req = request.GET
    # print(req)
    name = req['name']
    # return HttpResponse('hi')
    return render(request, 'interact.html', {'name':name})
