from rest_framework_swagger.views import get_swagger_view

from photos import views
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from photos.views import registration

router = routers.DefaultRouter()
router.register(r'photos', views.PhotoViewSet)

schema_view = get_swagger_view(title="Photos API")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', registration, name='register'),
    path('docss/', schema_view),
]