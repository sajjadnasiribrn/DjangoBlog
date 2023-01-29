from django import forms
from django.shortcuts import get_object_or_404

from blog.middlewares import get_request
from blog.models import Post
from comment.models import Comment


class CommentForm(forms.ModelForm):
    body = forms.CharField(max_length=700, min_length=1, required=True, error_messages={
        'min_length': 'طول عبارت جست و جو باید بیش از 3 کاراکتر باشد.'
    })
    post = forms.IntegerField(required=True)
    parent = forms.IntegerField(required=False)

    author = forms.IntegerField(required=False)

    class Meta:
        model = Comment
        fields = ['body', 'post', 'parent', 'author']

    def clean_author(self):
        if get_request().user.is_authenticated:
            return get_request().user

        return None

    def clean_post(self):
        if self.cleaned_data["post"]:
            return get_object_or_404(Post.objects.all(), pk=self.cleaned_data['post'])

        return None

    def clean_parent(self):
        if self.cleaned_data["parent"]:
            return get_object_or_404(Comment.objects.all(), pk=self.cleaned_data['parent'])

        return None
