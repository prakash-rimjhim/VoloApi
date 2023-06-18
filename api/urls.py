
from django.contrib import admin
from django.urls import include, path
from api.views import DataViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Data', DataViewSet)


urlpatterns = [
    path('',include(router.urls)),
]
