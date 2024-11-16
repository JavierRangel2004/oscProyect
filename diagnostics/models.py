# diagnostics/models.py

from django.db import models
from organizations.models import Organization

class Question(models.Model):
    text = models.TextField()
    choices = models.JSONField()

    def __str__(self):
        return self.text

class Diagnostic(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    questions = models.ManyToManyField(Question, related_name='diagnostics')

    def __str__(self):
        return self.name

class DiagnosticResult(models.Model):
    diagnostic = models.ForeignKey(
        Diagnostic,
        on_delete=models.CASCADE,
        related_name='results'
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='diagnostic_results'
    )
    date_taken = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()
    results = models.JSONField()

    def __str__(self):
        return f"{self.organization.name} - {self.diagnostic.name} - {self.score}"
