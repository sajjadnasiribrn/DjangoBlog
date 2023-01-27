from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST

from blog.forms import AllPostsForm, BookmarkForm
from blog.models import Post


# Create your views here.
def show(request, slug, pid):
    return render(request, 'blog/show-post.html', {'post': Post.get_single_post(slug=slug, pk=pid)})


def all_posts(request):
    form = AllPostsForm(request.GET)
    if form.is_valid():
        data = form.cleaned_data
        pages = Post.get_all_posts_with_paginate_and_search(data['per_page'], data['query'])
        page = pages.get_page(data['page'])
        return render(request, 'blog/all-posts.html', {
            'posts': page.object_list,
            'range': list(pages.get_elided_page_range(data['page'], on_each_side=1, on_ends=1)),
            'current_page': page.number,
            'per_page': pages.per_page,
            'query': data['query'],
            'page_count': pages.num_pages
        })
    else:
        messages.add_message(request, messages.ERROR, form.errors['query'])
        return redirect(reverse('blog:all-posts'))


@login_required
@require_POST
def bookmark(request):
    form = BookmarkForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        post = data['post']
        is_bookmarked = data['is_bookmarked']
        print(is_bookmarked)
        if is_bookmarked:
            post.detach_bookmarks()
        else:
            post.attach_bookmarks()
        return redirect(post.get_absolute_url())

    else:
        return HttpResponseBadRequest(form.errors)
