# coding:utf-8

from django.contrib import admin
from django.urls import path, include
from app.dashboard import urls as dashboard_urls
from app.client import urls as clien_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include(dashboard_urls)),
    path('client/', include(clien_urls)),
]
