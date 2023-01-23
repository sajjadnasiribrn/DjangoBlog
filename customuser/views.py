from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.shortcuts import render, redirect
from customuser.middlewares import guest


# Create your views here.
@require_GET
@guest
def login_or_register(request):
    return render(request, 'customuser/login-or-register.html')


@login_required
@require_POST
def logout_user(request):
    logout(request)
    return redirect("website:home")


@login_required
def back_from_google(request):
    list(messages.get_messages(request))
    messages.success(request, 'شما با موفقیت وارد شدید!')
    return redirect('blog:all-posts')
