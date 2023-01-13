from django.shortcuts import render, get_object_or_404

from blog.models import Post


# Create your views here.
def show(request, slug, pid):
    return render(request, 'blog/show-post.html', {'post': Post.get_single_post(slug=slug, pk=pid)})
