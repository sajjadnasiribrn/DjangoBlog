from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', index, name='home')
]
