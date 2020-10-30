# coding:utf-8

from django.urls import path
from .views.base import Index
from .views.auth import Login, AdminManager, Logout

urlpatterns = [
    path('', Index.as_view(), name='dashboard_index'),
    path('login', Login.as_view(), name='dashboard_login'),
    path('admin/manager', AdminManager.as_view(), name='admin_manager'),
    path('logout', Logout.as_view(), name='logout')
]
