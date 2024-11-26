# osc_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Set the 'View Site' link in the Django admin
admin.site.site_url = 'http://localhost:4200/home'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('organizations/', include('organizations.urls')),
    path('projects/', include('projects.urls'))
    # path('forum/', include('forum.urls')),
    # path('recognitions/', include('recognitions.urls')),
    # path('resources/', include('resources.urls')),
    # path('diagnostics/', include('diagnostics.urls')),
    # path('users/', include('users.urls')),
]


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)