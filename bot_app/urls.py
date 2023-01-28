import djoser as djoser
from django.contrib import admin
from django.urls import path, include, re_path

from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'userlist', UserViewSets)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
]
