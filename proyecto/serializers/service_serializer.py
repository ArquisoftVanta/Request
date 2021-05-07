from rest_framework import serializers
from proyecto.models.service_model import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['service_id','user_id','vehicle_id','date','time','state_service','service_value','places']
