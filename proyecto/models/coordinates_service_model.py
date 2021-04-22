from django.db import models
from .request_model import Service

class Coordinates_Service(models.Model):

    coordinates_id = models.AutoField(primary_key = True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    order = models.IntegerField()

    class Meta:
        app_label = 'vanta'
