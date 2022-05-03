from django.shortcuts import render, HttpResponse


def sub(request):
    #return HttpResponse('<h1>sub</h1>')
    return render(request, 'sub.html')


def sub_res(request):
    dict1 = request.GET
    num1 = int(dict1['num1'])
    num2 = int(dict1['num2'])
    return render(request, 'sub.html', {'res':num1-num2})
