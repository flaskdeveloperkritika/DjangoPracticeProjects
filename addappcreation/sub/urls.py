from django.urls import path
from sub.views import home, hi


urlpatterns = [
    path('', home),
    path('hi/', hi)
]