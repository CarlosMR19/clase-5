from rest_framework import viewsets 
from .models import Motos
from .serializers import MotosSerializer

class MotosViewSet(viewsets.ModelViewSet):
    queryset = Motos.objects.all()
    serializer_class = MotosSerializer
