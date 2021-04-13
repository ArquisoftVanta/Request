from django.db import models
class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    vehicle_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    state_service = models.BooleanField(default= True)
    registry_request = models.DateTimeField()

    class Meta:
        app_label = 'vanta'
