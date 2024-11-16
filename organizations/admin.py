# organizations/admin.py

from django.contrib import admin
from .models import Organization, Category, Recognition

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category')

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email', 'phone_number', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description', 'contact_email')

@admin.register(Recognition)
class RecognitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'date_awarded')
    list_filter = ('date_awarded',)
    search_fields = ('name', 'organization__name')
