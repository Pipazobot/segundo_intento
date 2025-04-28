from rest_framework import viewsets
from .models import cuaderno
from .serializers import cuadernoSerializer

class cuadernoViewSet(viewsets.ModelViewSet):
    queryset = cuaderno.objects.all()
    serializer_class = cuadernoSerializer

