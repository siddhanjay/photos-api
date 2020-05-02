from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from photos.models import Photo
from photos.serializers import PhotoSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows photos to be viewed or edited.
    """
    queryset = Photo.objects.all().order_by('publish_time')
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticated]

    lookup_field = 'id'

    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['user']
    ordering_fields = ['publish_time']
    search_fields = ['caption']
