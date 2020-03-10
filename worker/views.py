from django.shortcuts import render
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry
from rest_framework import viewsets
from worker.models import Mapdata
from worker.serializer import Mapdatserializer

# Create your views here.

class Workers(viewsets.ModelViewSet):
    queryset=Mapdata.objects.all()
    serializer_class=Mapdatserializer

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     lattitude=self.request.query_params.get('lat',None)
    #     longitude=self.request.query_params.get('lng',None)

    #     if lattitude and longitude:
    #         pnt=GEOSGeometry('POINT('+str(longitude)+' '+str(lattitude)+')',srid=4326)
    #         qs=qs.filter(location__distance_lte=(pnt, D(m=500))).annotate(distances=Distance('location',pnt)).order_by('distances')
    #         return qs