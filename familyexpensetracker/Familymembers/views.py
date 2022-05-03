from django.shortcuts import render, redirect
from Familymembers.models import FamilyMember
from django.views.decorators.csrf import csrf_exempt


def addmemberpage(request):
    return render(request, 'addmember.html')


@csrf_exempt
def savedata(request):
    dict1 = request.POST
    images = request.FILES
    name = dict1['name']
    mobile = dict1['mobile']
    work = dict1['work']
    income = dict1['income']
    prof_image = images['image']
    obj = FamilyMember()
    obj.name = name
    obj.mobile = mobile
    obj.work = work
    obj.income = income
    obj.profile_image = prof_image
    obj.pay_slip = images['payslip']
    obj.save()
    return redirect('/')