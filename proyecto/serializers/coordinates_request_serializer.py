from rest_framework import serializers
from proyecto.models.coordinates_request_model import Coordinates_Request


class CoordinatesRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates_Request
        fields = ['coordinates_id','request','lat','lng','address','type','order']

