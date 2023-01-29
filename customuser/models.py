from django.core.paginator import Paginator
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


# from blog.models import Post


class User(AbstractUser):
    bookmarks = models.ManyToManyField('blog.Post', blank=True)

    class Meta:
        db_table = 'auth_user'

    def get_paginate_bookmarks(self, per_page: int):
        return Paginator(self.bookmarks.all(), per_page)
