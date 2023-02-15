

from django.urls import path,include
from .views import *
urlpatterns = [
  
    path('', index, name='index'),
    path('get_locations/', get_locations, name='get_locations'),
    path('get_business_plans/', get_business_plans, name='get_business_plans'),
    path('get_values/', get_values, name='get_values'),
    
]
