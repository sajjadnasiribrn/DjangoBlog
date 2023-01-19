from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from website.forms import ContactForm


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'website/index.html')


def contact(request: HttpRequest) -> HttpResponse:
    context = {}
    print(request.POST)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'پیام شما با موفقیت دریافت شد.')
        else:
            context.update({'form': form})

    return render(request, 'website/contact.html', context=context)
