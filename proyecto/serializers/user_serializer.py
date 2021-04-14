from rest_framework import serializers
from proyecto.models.user_model import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['user_id','name','doc','phone','university_id','mail','password','rh','picture','registry_date']