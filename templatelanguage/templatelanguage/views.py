from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def color(request):
    dict1 = request.GET
    name = dict1['color']
    list1 = ['shirt', 'shoes', 'tie', 'cap']
    list2 = ['abc', 'xyz', 'pqr']
    out = {'name':name,
           'garments':list1}
    return render(request, 'color.html', out)


def list(request):
    li = ["abc", "xyz", "pqr"]
    data = {'list':li}
    return render(request, 'list.html', data)