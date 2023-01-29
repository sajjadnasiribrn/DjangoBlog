from django.db import models

from blog.models import Post
from customuser.models import User
from jalali_date import datetime2jalali


class Approved(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Status.APPROVED)


# Create your models here.
class Status(models.TextChoices):
    APPROVED = 'ap', 'Approved'
    REJECTED = 're', 'rejected'


class Comment(models.Model):
    body = models.TextField(max_length=700)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.REJECTED)

    # RELATIONS
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)

    # DATE TIMES
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # MANAGERS
    default_manager = models.Manager()
    objects = Approved()

    @property
    def jalali_created_at(self):
        return datetime2jalali(self.created_at).strftime('%Y/%m/%d')

    class Meta:
        ordering = ['-created_at']
        get_latest_by = ['-created_at']
