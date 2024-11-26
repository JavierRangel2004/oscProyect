# recognitions/serializers.py

from rest_framework import serializers
from .models import Recognition
from organizations.serializers import OrganizationSerializer

class RecognitionSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(read_only=True)
    
    class Meta:
        model = Recognition
        fields = ['id', 'name', 'description', 'date_awarded', 'organization']
