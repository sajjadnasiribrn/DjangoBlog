from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST

from comment.forms import CommentForm
from comment.models import Comment


# Create your views here.
@require_POST
def create(request, pid, slug, parent=None):
    data = request.POST.copy()
    data['post'] = pid
    data['parent'] = parent
    form = CommentForm(data)

    if form.is_valid():
        form.save()
        messages.success(request, 'نظر شما با موفقیت دریافت شد و پس از تایید منتشر می شود.')

    return redirect(reverse('blog:show-post', kwargs={'slug': slug, 'pid': pid}))


@require_POST
@login_required
def delete(request, id):
    comment = get_object_or_404(Comment.objects.select_related('post').select_related('author').all(), pk=id)
    author = comment.author
    post = comment.post

    if author.id != request.user.id:
        raise Exception('403!')

    comment.delete()
    messages.success(request, 'نظر شما حذف شد.')
    return redirect(reverse('blog:show-post', kwargs={'slug': post.slug, 'pid': post.id}))
