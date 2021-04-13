from django.db import models
from .service_model import Service
class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE,blank=True, null=True)
    active = models.BooleanField(default= False)
    registry_request = models.DateTimeField()

    class Meta:
        app_label = 'vanta'
