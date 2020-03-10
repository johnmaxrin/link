from django.contrib.gis.db import models
# Create your models here.

class Mapdata(models.Model):
    uid=models.CharField(max_length=250,default='SOME STRING')
    lattitude=models.CharField(max_length=250,default='SOME STRING')
    longitude=models.CharField(max_length=250,default='SOME STRING')
    avatar=models.URLField(max_length=250)
    name = models.CharField(max_length=100,default='SOME STRING')
    
    location = models.PointField()

    


