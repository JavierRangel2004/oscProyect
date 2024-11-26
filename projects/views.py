# projects/views.py

from rest_framework import viewsets
from .models import Project, Image
from .serializers import ProjectSerializer, ImageSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.all()
        organization = self.request.query_params.get('organization', None)
        if organization is not None:
            queryset = queryset.filter(organization__id=organization)
        return queryset


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
