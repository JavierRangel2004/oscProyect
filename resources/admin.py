# resources/admin.py

from django.contrib import admin
from .models import Resource

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'added_by', 'date_added')
    list_filter = ('date_added',)
    search_fields = ('title', 'description', 'added_by__username')
