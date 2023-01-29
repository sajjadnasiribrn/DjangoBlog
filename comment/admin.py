from django.contrib import admin

from comment.models import Comment


# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    empty_value_display = '---'
    list_display = ('body', 'status', 'created_at',
                    'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('body',)


admin.site.register(Comment, CommentAdmin)
