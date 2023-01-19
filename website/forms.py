from django import forms

from website.models import Contact


class ContactForm(forms.ModelForm):
    # captcha = CaptchaField()
    name = forms.CharField(max_length=255, error_messages={
        'required': 'لطفا نام را وارد کنید.'
    })
    email = forms.EmailField(max_length=300, error_messages={
        'required': 'لطفا ایمیل خود را وارد کنید.'
    })
    message = forms.CharField(widget=forms.Textarea(), error_messages={
        'required': 'متن پیام الزامی است.'
    })

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
