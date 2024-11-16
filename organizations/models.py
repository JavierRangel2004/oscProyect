# organizations/models.py

from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    parent_category = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='subcategories'
    )

    def __str__(self):
        return self.name

class Recognition(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_awarded = models.DateTimeField()
    organization = models.ForeignKey(
        'Organization',
        on_delete=models.CASCADE,
        related_name='recognitions'
    )

    def __str__(self):
        return f"{self.name} - {self.organization.name}"

class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    website = models.URLField(null=True, blank=True)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    address = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category, related_name='organizations')
    date_added = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
