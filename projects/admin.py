# projects/admin.py

from django.contrib import admin
from .models import Project, Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'is_active', 'date_added')
    list_filter = ('is_active', 'date_added')
    search_fields = ('name', 'description', 'organization__name')
    filter_horizontal = ('categories', 'images')
