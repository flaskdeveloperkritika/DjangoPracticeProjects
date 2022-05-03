from django.urls import path
from mul.views import mul, mul_res

urlpatterns = [
    path('', mul),
    path('byebye', mul_res)
]