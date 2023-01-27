from django import forms
from django.shortcuts import get_object_or_404

from blog.models import Post


class AllPostsForm(forms.Form):
    query = forms.CharField(max_length=255, min_length=3, required=False, error_messages={
        'min_length': 'طول عبارت جست و جو باید بیش از 3 کاراکتر باشد.'
    })
    page = forms.IntegerField(required=False)
    per_page = forms.IntegerField(required=False)

    def clean_page(self):
        if self.cleaned_data['page']:
            return self.cleaned_data['page']
        else:
            return 1

    def clean_per_page(self):
        if self.cleaned_data['per_page']:
            return self.cleaned_data['per_page']
        else:
            return 5


class BookmarkForm(forms.Form):
    post = forms.IntegerField(required=True)
    is_bookmarked = forms.BooleanField(required=False)

    def clean_post(self):
        return get_object_or_404(Post.objects.all(), pk=self.cleaned_data['post'])
