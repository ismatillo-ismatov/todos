from rest_framework import serializers
from .models import Description


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ['id','weather','temprature','created_on']