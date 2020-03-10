from worker.models import Mapdata
from rest_framework import serializers

class Mapdatserializer(serializers.ModelSerializer):
    class Meta:
        model=Mapdata
        fields='__all__'