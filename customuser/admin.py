from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from customuser.models import User


# class CustomUserAdmin(UserAdmin):
#     fieldsets = UserAdmin.fieldsets + (
#         ('Additional info', {'fields': ('phone', 'address')}),
#     )


admin.site.register(User)
