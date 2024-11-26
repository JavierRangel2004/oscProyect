# projects/views.py

from rest_framework import viewsets
from .models import Project, Image
from .serializers import ProjectSerializer, ImageSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
