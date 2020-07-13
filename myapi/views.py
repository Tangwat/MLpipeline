from rest_framework import viewsets

from .serializers import FarmerSerializer
from .models import Farmer


class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all().order_by('name')
    serializer_class = FarmerSerializer
