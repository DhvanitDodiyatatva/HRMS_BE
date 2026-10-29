"""
API v1 URL aggregation
"""

from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    """
    Public health check endpoint.
    Used by frontend, docker healthchecks, and load balancers.
    """
    return Response({
        'status': 'healthy',
        'service': 'HRMS Backend API',
        'version': '1.0.0',
    })


urlpatterns = [
    path('health/', health_check, name='health-check'),
    path('auth/', include('apps.authentication.urls')),
    path('employees/', include('apps.employees.urls')),
    path('attendance/', include('apps.attendance.urls')),
    path('leave/', include('apps.leave.urls')),
    path('salary/', include('apps.salary.urls')),
    path('resignation/', include('apps.resignation.urls')),
    path('transfer/', include('apps.transfer.urls')),
    path('master/', include('apps.master_data.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
    path('notifications/', include('apps.notifications.urls')),
]
