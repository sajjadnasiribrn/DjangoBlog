from django.urls import path
from auth.views import *

app_name = 'auth'

urlpatterns = [
    path('', login_or_register, name='login-or-register'),
    path('/logout', logout_user, name='logout'),
    path('/back-from-google', back_from_google, name='back-from-google')
]