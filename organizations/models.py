# organizations/models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    address = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category)
    date_added = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    social_media_1 = models.CharField(max_length=250, null=True, blank=True)
    social_media_2 = models.CharField(max_length=250, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)  # Increased max_length
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name
