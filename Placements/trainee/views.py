from django.shortcuts import render, redirect
from trainee.models import Trainee


def home(request):
    return render(request, 'register.html')


def save_method(request):
    dict1 = request.POST
    name = dict1['username']
    regid = int(dict1['regid'])
    phone = int(dict1['phonenumber'])
    subject = dict1['subject']
    obj = Trainee()
    obj.trainee_name = name
    obj.reg_id = regid
    obj.phone_number = phone
    obj.subject = subject
    obj.save()
    return redirect('/register')



