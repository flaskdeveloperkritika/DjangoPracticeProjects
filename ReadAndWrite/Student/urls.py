from django.urls import path
from Student.views import *   # register_page, register_user, get_records


urlpatterns = [
    path('register', register_page),
    path('registeruser', register_user),
    path('records', get_records),
    path('univsearch', send_search_univ),
    path('getresultsbaseduniv', getunivresults),
    path('branchsearch', send_branch_search),
    path('getresultsbasedbranch', getbranchresults)
]