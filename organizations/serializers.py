# organizations/serializers.py

from rest_framework import serializers
from .models import Organization, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class OrganizationSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Organization
        fields = [
            'id', 'name', 'description', 'website', 'logo',
            'address', 'categories', 'date_added', 'is_active',
            'social_media_1', 'social_media_2', 'phone_number', 'email'
        ]
