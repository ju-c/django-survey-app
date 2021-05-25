from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # User management
    path('accounts/', include('django.contrib.auth.urls')),
    # Local apps
    path('accounts/', include('accounts.urls')),
    path('', include('surveys.urls')),
]
