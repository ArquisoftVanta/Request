from django.db import models
class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length= 50)
    vehicle_id = models.CharField(max_length= 6)
    date = models.DateField()
    time = models.TimeField()
    state_service = models.BooleanField(default= True)
    service_value = models.FloatField()
    places = models.IntegerField()

    class Meta:
        app_label = 'vanta'
