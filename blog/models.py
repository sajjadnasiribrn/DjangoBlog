from datetime import datetime
from html import unescape

from blog.middlewares import get_request
from customuser.models import User
from django.core.paginator import Paginator
from django.db import models
from django.db.models import F, Q
from django.shortcuts import get_object_or_404
from django_ckeditor_5.fields import CKEditor5Field
from jalali_date import datetime2jalali
from django.urls import reverse
from django.utils.html import strip_tags
import math
from taggit.managers import TaggableManager


class Published(models.Manager):
    def get_queryset(self):
        return super(Published, self).get_queryset().filter(status='pu').filter(published_date__lt=datetime.now())


# Create your models here.
class Status(models.TextChoices):
    PUBLISHED = 'pu', 'Published'
    DRAFT = 'dr', 'Draft'


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = CKEditor5Field('Text', config_name='extends')
    slug = models.SlugField(max_length=255, unique=True)
    tags = TaggableManager()
    image = models.ImageField(upload_to='blog/', max_length=5000, null=True, blank=True)
    view_count = models.IntegerField(default=0)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.PUBLISHED)
    login_required = models.BooleanField(default=False)
    published_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # RELATIONS
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    categories = models.ManyToManyField(Category)

    # MANAGERS
    default_manager = models.Manager()
    objects = Published()

    # CLASS METHODS
    @classmethod
    def get_single_post(cls, slug: str, pk: int):
        post = get_object_or_404(
            cls.objects.filter(slug=slug).prefetch_related('categories'), pk=pk)
        post.view_count = F('view_count') + 1
        post.save()
        return post

    @classmethod
    def get_all_posts_with_paginate_and_search(cls, per_page: int, query: str):
        builder = cls.objects.all().prefetch_related('categories')
        if query:
            builder = builder.filter(
                Q(title__contains=query) |
                Q(content__contains=query) |
                Q(categories__name__contains=query)
            ).distinct()
        return Paginator(builder, per_page)

    def attach_bookmarks(self):
        get_request().user.bookmarks.add(self)

    def detach_bookmarks(self):
        get_request().user.bookmarks.remove(self)

    @property
    def is_bookmarked(self):
        user = get_request().user
        if user.is_anonymous:
            return False

        return User.objects.filter(bookmarks=self).filter(id=user.id).exists()

    # ATTRIBUTES
    @property
    def min_read(self):
        string = self.title + unescape(strip_tags(self.content))
        total_words = len(string.split())
        return math.ceil(total_words / 80)

    @property
    def jalali_created_at(self):
        return datetime2jalali(self.created_at).strftime('%Y/%m/%d')

    @property
    def description(self):
        return self.content[:150] + '...'

    def get_absolute_url(self):
        return reverse('blog:show-post', kwargs={'slug': self.slug, 'pid': self.id})

    class Meta:
        ordering = ['-created_at']
        get_latest_by = ['-created_at']

    def __str__(self):
        return self.title
