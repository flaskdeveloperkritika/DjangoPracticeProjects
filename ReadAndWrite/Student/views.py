from django.shortcuts import render, redirect, HttpResponse
from Student.models import Student


def register_page(request):
    return render(request, 'register.html')


def register_user(request):
    dict1 = request.GET
    name = dict1['name']
    branch = dict1['branch']
    univ = dict1['univ']
    obj = Student()
    obj.student_name = name
    obj.student_branch = branch
    obj.student_univ = univ
    obj.save()
    return redirect('/student/register')


def get_records(request):
    objects = Student.objects.all()
    print(objects)
    return render(request, 'student_records.html', {'obj':objects})


def send_search_univ(request):
    return render(request, 'search_univ.html')


def getunivresults(request):
    dict1 = request.GET
    univ = dict1['univ']
    objects = Student.objects.filter(student_univ=univ)
    return render(request, 'student_records.html', {'obj': objects})


def send_branch_search(request):
    return render(request, 'searchbranch.html')


def getbranchresults(request):
    dict1 = request.GET
    branch = dict1['branch']
    objects = Student.objects.filter(student_branch=branch)
    return render(request, 'student_records.html', {'obj': objects})


