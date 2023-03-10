from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST, require_GET

from blog.forms import AllPostsForm, BookmarkForm, RateForm
from blog.models import Post, Category


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
        if is_bookmarked:
            post.detach_bookmarks()
            messages.add_message(request, messages.SUCCESS, 'نوشته موردنظر از ذخیره ها حذف شد.')
        else:
            post.attach_bookmarks()
            messages.add_message(request, messages.SUCCESS, 'نوشته موردنظر ذخیره شد.')
        return redirect(post.get_absolute_url())

    else:
        return HttpResponseBadRequest(form.errors)


@login_required
@require_GET
def bookmarks(request):
    form = AllPostsForm(request.GET)
    if form.is_valid():
        data = form.cleaned_data
        pages = request.user.get_paginate_bookmarks(data['per_page'])
        page = pages.get_page(data['page'])
        return render(request, 'blog/bookmarks.html', {
            'posts': page.object_list,
            'range': list(pages.get_elided_page_range(data['page'], on_each_side=1, on_ends=1)),
            'current_page': page.number,
            'per_page': pages.per_page,
            'page_count': pages.num_pages
        })
    else:
        messages.add_message(request, messages.ERROR, 'خطایی پیش آمده. لطفا دوباره امتحان کنید.')
        return redirect(reverse('blog:bookmarks'))


@require_GET
def show_category_posts(request, slug, cid):
    form = AllPostsForm(request.GET)
    if form.is_valid():
        data = form.cleaned_data
        category_data = Category.get_category_posts_with_paginate(cid=cid, per_page=data['per_page'])
        pages = category_data['posts']

        page = pages.get_page(data['page'])

        return render(request, 'blog/show-category-posts.html', {
            'posts': page.object_list,
            'range': list(pages.get_elided_page_range(data['page'], on_each_side=1, on_ends=1)),
            'current_page': page.number,
            'per_page': pages.per_page,
            'page_count': pages.num_pages,
            'category': category_data['category']
        })
    else:
        messages.add_message(request, messages.ERROR, 'خطایی پیش آمده. لطفا دوباره امتحان کنید.')
        return redirect(reverse('blog:show-category-posts', {'cid': cid, 'slug': slug}))


def rate(request, pid, rate):
    data = request.POST.copy()
    data['post'] = pid
    data['rate'] = rate
    form = RateForm(data)

    if form.is_valid():
        form.save()
        return JsonResponse({
            "status": True,
            "message": "با تشکر از نظر شما!",
            "rate": rate
        })

    return redirect(reverse('website:home'))

