from django.urls import path
from .views import *


urlpatterns=[
    path('',short_url, name='short_url'),
    path('<str:s_url>', redirect_to_long_url, name='redirect'),
    path('list/',list_records, name='list'),
]