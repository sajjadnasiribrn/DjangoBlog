from django import template

from blog.models import Post

register = template.Library()


@register.simple_tag()
def show_group_posts(take=5):
    return Post.objects.all().prefetch_related('categories').order_by('-view_count')[:take]


@register.filter()
def is_digit(value):
    return type(value) == int
