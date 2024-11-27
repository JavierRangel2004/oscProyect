# projects/models.py

from django.db import models
from organizations.models import Organization, Category

class Image(models.Model):
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return self.image.name

class Project(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='projects'
    )
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    objectives = models.TextField(null=True, blank=True)
    achievements = models.TextField(null=True, blank=True)
    participation_methods = models.TextField(null=True, blank=True)
    images = models.ManyToManyField(Image, blank=True)
    categories = models.ManyToManyField(Category)
    date_added = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

