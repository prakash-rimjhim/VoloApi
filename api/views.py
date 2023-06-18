from django.shortcuts import render
from rest_framework import viewsets
from api.models import Data
from api.serializers import DataSerializer

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
