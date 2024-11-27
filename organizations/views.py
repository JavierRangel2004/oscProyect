# organizations/views.py

from rest_framework import viewsets, status
from .models import Organization, Category
from .serializers import OrganizationSerializer, CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
import csv
import os
from django.conf import settings
from rest_framework.views import APIView

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OrganizationRequestView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        data = request.data

        # Prepare data to write to CSV
        request_data = {
            'name': data.get('name', ''),
            'description': data.get('description', ''),
            'website': data.get('website', ''),
            'address': data.get('address', ''),
            'categories': data.getlist('categories'),
            'social_media': data.get('social_media', ''),
            'phone_number': data.get('phone_number', ''),
            'email': data.get('email', ''),
        }

        # Handle logo file
        logo = request.FILES.get('logo')
        if logo:
            logo_path = os.path.join('organization_requests', logo.name)
            logo_full_path = os.path.join(settings.MEDIA_ROOT, logo_path)
            os.makedirs(os.path.dirname(logo_full_path), exist_ok=True)
            with open(logo_full_path, 'wb+') as destination:
                for chunk in logo.chunks():
                    destination.write(chunk)
            request_data['logo'] = logo_path
        else:
            request_data['logo'] = ''

        # Write data to CSV
        csv_file_path = os.path.join(settings.MEDIA_ROOT, 'organization_requests.csv')
        file_exists = os.path.isfile(csv_file_path)
        with open(csv_file_path, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = [
                'name',
                'description',
                'website',
                'logo',
                'address',
                'categories',
                'social_media',
                'phone_number',
                'email'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(request_data)

        return Response({'message': 'Solicitud recibida.'}, status=status.HTTP_200_OK)
