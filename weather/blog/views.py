from django.shortcuts import render
from rest_framework import viewsets
from .models import Description
from .serializer import WeatherSerializer

class weatherViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Description.objects.all()
    serializer_class = WeatherSerializer