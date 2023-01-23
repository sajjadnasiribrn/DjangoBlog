from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# from blog.models import Post


class User(AbstractUser):

    bookmarks = models.ManyToManyField('blog.Post', blank=True)

    class Meta:
        db_table = 'auth_user'
