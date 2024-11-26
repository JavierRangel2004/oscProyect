# organizations/views.py

from rest_framework import viewsets
from .models import Organization, Category
from .serializers import OrganizationSerializer, CategorySerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
