from django import template
from django.db.models import Q, Prefetch

from comment.models import Comment

register = template.Library()


@register.inclusion_tag('comment/comments.html')
def get_comments(post, request):
    return {
        'comments': Comment.objects
        .prefetch_related(Prefetch('comment_set', Comment.objects.all()))
        .filter(Q(post=post) & Q(parent=None)),
        'request': request,
        'post': post
    }
