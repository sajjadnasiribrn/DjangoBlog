from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('<str:slug>.p<int:pid>', show, name='show-post')
]
