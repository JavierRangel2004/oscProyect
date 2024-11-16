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
    description = models.TextField()
    objectives = models.TextField()
    achievements = models.TextField()
    participation_methods = models.TextField()
    images = models.ManyToManyField(Image, blank=True, related_name='projects')
    categories = models.ManyToManyField(Category, related_name='projects')
    date_added = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
