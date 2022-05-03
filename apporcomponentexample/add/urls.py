from django.urls import path
from add.views import add, add_res

urlpatterns = [
    path('', add),
    path('hello', add_res)
]