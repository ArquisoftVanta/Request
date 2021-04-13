from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    doc = models.CharField(max_length=15)
    phone = models.CharField(max_length=10)
    university_id = models.IntegerField()
    mail = models.CharField(max_length=30)
    password = models.CharField(max_length=200)
    rh = models.CharField(max_length=3)
    picture = models.CharField(max_length=100)
    registry_date = models.DateTimeField()

    class Meta:
        app_label = 'vanta'
