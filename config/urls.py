from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # User management
    path('accounts/', include('allauth.urls')),
    # Local apps
    path('', include('surveys.urls')),
]
