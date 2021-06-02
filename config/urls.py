from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path('anyminutenow/', admin.site.urls),
    # User management
    path('accounts/', include('allauth.urls')),
    # Local apps
    path('', include('surveys.urls')),
]
