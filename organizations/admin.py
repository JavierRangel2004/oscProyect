# organizations/admin.py

from django.contrib import admin
from .models import Organization, Category

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'email', 'phone_number', 'is_active')
    search_fields = ('name', 'address', 'email')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
