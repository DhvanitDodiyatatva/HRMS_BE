from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# TODO: Register attendance viewsets
# router.register(r'endpoint', ViewSet, basename='endpoint')

urlpatterns = router.urls

