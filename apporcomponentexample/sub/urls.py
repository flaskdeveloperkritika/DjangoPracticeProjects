from django.urls import path
from sub.views import sub, sub_res

urlpatterns = [
    path('', sub),
    path('hi', sub_res)
]