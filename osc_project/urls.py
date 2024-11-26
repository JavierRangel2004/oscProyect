# osc_project/urls.py

from django.contrib import admin
from django.urls import path, include

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
