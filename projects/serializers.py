# projects/serializers.py

from rest_framework import serializers
from .models import Project, Image
from organizations.serializers import CategorySerializer, OrganizationSerializer

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']

class ProjectSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = [
            'id', 'organization', 'name', 'description',
            'objectives', 'achievements', 'participation_methods',
            'images', 'categories', 'date_added', 'is_active'
        ]
