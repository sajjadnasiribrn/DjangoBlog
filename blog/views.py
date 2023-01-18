from pprint import pprint

from django.shortcuts import render, get_object_or_404

from blog.models import Post


# Create your views here.
def show(request, slug, pid):
    return render(request, 'blog/show-post.html', {'post': Post.get_single_post(slug=slug, pk=pid)})


def all_posts(request):
    pages = Post.get_all_posts_with_paginate(request.GET.get('per_page', 5))
    current_page = request.GET.get('page', 1)
    page = pages.get_page(current_page)
    return render(request, 'blog/all-posts.html', {
        'posts': page.object_list,
        'range': list(pages.get_elided_page_range(current_page, on_each_side=1, on_ends=2)),
        'current_page': page.number,
        'per_page': pages.per_page
    })
