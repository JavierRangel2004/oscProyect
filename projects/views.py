# projects/views.py

from rest_framework import viewsets
from .models import Project, Image
from .serializers import ProjectSerializer, ImageSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.all()
        category_id = self.request.query_params.get('category', None)
        organization_id = self.request.query_params.get('organization', None)

        if category_id is not None:
            queryset = queryset.filter(categories__id=category_id)
        
        if organization_id is not None:
            queryset = queryset.filter(organization__id=organization_id)
        
        return queryset

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
