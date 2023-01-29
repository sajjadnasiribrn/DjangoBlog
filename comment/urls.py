from django.urls import path, re_path
from comment.views import *

app_name = 'comment'

urlpatterns = [
    re_path(r'^create/(?P<pid>[0-9]+)/(?P<slug>[-a-zA-Z0-9_]+)/(?P<parent>[0-9]+)?', create, name='create'),
    path('delete/<int:id>', delete, name='delete'),
]
