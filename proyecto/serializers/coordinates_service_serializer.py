from rest_framework import serializers
from proyecto.models.coordinates_service_model import Coordinates_Service


class CoordinatesServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates_Service
        fields = ['coordinates_id','service','lat','lng','address','type']

