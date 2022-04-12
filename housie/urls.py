from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('delete/',access_ses,name="delete"),
    path('recent/',numbers,name="recent"),
    path('get_response/',get_response,name='get_response')
]