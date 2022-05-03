from django.shortcuts import render, HttpResponse


def add(request):
    return render(request, 'add.html')


def add_num(request):
    # print(request.GET)
    dict1 = request.GET
    # num1 = dict1['num1']
    # num2 = dict1['num2']
    num1 = int(dict1['num1'])
    num2 = int(dict1['num2'])
    # print(num1)
    # print(num2)
    res = num1 + num2
    print(res)
    return render(request, 'out.html', {'out':res})






# Basedir/templates