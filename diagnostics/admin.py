# diagnostics/admin.py

from django.contrib import admin
from .models import Diagnostic, Question, DiagnosticResult

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text',)
    search_fields = ('text',)

@admin.register(Diagnostic)
class DiagnosticAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    filter_horizontal = ('questions',)

@admin.register(DiagnosticResult)
class DiagnosticResultAdmin(admin.ModelAdmin):
    list_display = ('diagnostic', 'organization', 'score', 'date_taken')
    list_filter = ('diagnostic', 'organization', 'date_taken')
    search_fields = ('diagnostic__name', 'organization__name')
