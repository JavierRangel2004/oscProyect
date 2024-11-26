# organizations/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrganizationViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet, basename='organization')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
