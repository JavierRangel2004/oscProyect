# resources/models.py

from django.db import models
from users.models import User

class Resource(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='resources/files/', null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='resources_added'
    )

    def __str__(self):
        return self.title
