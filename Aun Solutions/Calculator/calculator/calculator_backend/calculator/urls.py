from django.urls import path
from .views import *

urlpatterns = [
    path('calculate/', calculate, name = 'calculate'),
    path('history/', history, name = 'history'),
    path('delete/<int:exp_id>', delete_record, name = 'delete_record')
]