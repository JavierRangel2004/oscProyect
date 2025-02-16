# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('is_admin',)}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_admin', 'is_staff')

admin.site.register(User, UserAdmin)
