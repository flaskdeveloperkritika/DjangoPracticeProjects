from django.shortcuts import render


def max(request):
    dict1 = request.GET
    num1 = dict1['num1']
    num2 = dict1['num2']
    if num1 > num2:
        print('num1 is greater')
        return num1
    else:
        print('num2 is greater')
        return num2
    return render(request, 'max.html', )