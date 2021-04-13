from django.db import models
from .request_model import Request

class Coordinates_Request(models.Model):

    coordinates_id = models.AutoField(primary_key = True)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    type = models.IntegerField()

    class Meta:
        app_label = 'vanta'
