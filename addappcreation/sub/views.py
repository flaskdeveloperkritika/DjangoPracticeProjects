from django.shortcuts import render


def home(request):
    return render(request, 'sub.html')


def hi(request):
    di2 = request.GET
    num1 = int(di2['num1'])
    num2 = int(di2['num2'])
    return render(request, 'sub.html', {'resl':num1-num2})