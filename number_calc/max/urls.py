from django.urls import path
from max.views import max


urlpatterns = [
    path('', max)
]