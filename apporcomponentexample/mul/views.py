from django.shortcuts import render, HttpResponse


def mul(request):
    #return HttpResponse('<h1>mul</h1>')
    return render(request, 'mul.html')


def mul_res(request):
    dict1 = request.GET
    num1 = int(dict1['num1'])
    num2 = int(dict1['num2'])
    return render(request, 'mul.html', {'res':num1*num2})