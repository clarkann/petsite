from rest_framework import viewsets
from adoption.models import Pet, AdoptionApplication 
from .serializers import PetSerializer, AdoptionApplicationSerializer

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class AdoptionApplicationViewSet(viewsets.ModelViewSet):
    queryset = AdoptionApplication.objects.all()
    serializer_class = AdoptionApplicationSerializer

