# recognitions/models.py

from django.db import models
from organizations.models import Organization

class Recognition(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_awarded = models.DateTimeField()
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='recognitions'
    )

    def __str__(self):
        return f"{self.name} - {self.organization.name}"
