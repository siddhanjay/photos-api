from django.conf.urls.static import static
from django.urls import path, include

from project import settings

urlpatterns = [
    path('', include('photos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
