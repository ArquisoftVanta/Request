from rest_framework import serializers
from proyecto.models.request_model import Request

class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = ['request_id','user_id','service_id','date','time','active','registry_request']
