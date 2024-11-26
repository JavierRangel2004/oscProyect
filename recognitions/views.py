# recognitions/views.py

from rest_framework import viewsets
from .models import Recognition
from .serializers import RecognitionSerializer

class RecognitionViewSet(viewsets.ModelViewSet):
    queryset = Recognition.objects.all()
    serializer_class = RecognitionSerializer
