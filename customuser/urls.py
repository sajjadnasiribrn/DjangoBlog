from django.urls import path
from customuser.views import *

app_name = 'customuser'

urlpatterns = [
    path('', login_or_register, name='login-or-register'),
    path('logout', logout_user, name='logout'),
    path('back-from-google', back_from_google, name='back-from-google')
]