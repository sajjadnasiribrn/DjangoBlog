from django.contrib import admin

from blog.models import Post, Category


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    empty_value_display = '---'
    list_display = ('title', 'slug', 'view_count', 'status', 'login_required', 'published_date', 'created_at',
                    'updated_at')
    list_filter = ('view_count', 'status', 'login_required')
    search_fields = ('title', 'slug', 'content')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
