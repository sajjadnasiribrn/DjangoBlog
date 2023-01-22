from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from blog.forms import AllPostsForm
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
