from django.contrib import admin
from django.urls import path, include
from django.conf import settings

api_prefix = settings.API_PREFIX

urlpatterns = [
    path('admin/', admin.site.urls),
    path(api_prefix, include('book.urls')),
]
