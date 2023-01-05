from django.contrib import admin
from website.models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('name', 'email', 'created_at')
    list_filter = ('email',)
    search_fields = ('name', 'message', 'email')


admin.site.register(Contact, ContactAdmin)
