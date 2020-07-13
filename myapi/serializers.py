from rest_framework import serializers
from .models import Farmer

class FarmerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Farmer
        fields = ('name', 'farmNature')