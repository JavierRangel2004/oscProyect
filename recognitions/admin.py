# recognitions/admin.py

from django.contrib import admin
from .models import Recognition

@admin.register(Recognition)
class RecognitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'date_awarded')
    search_fields = ('name', 'organization__name')
    list_filter = ('date_awarded', 'organization')
