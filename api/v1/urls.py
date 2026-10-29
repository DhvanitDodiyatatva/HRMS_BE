"""
API v1 URL aggregation
"""

from django.urls import path, include

urlpatterns = [
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
