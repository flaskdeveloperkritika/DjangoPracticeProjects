from django.urls import path
from Familymembers.views import *

urlpatterns = [
    path('addfamilymember', addmemberpage),
    path('savedata', savedata)
]