from rest_framework import generics
from cars.models import Car
from .serializers import CarSerializer

# Create your views here.

class CarAPIView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer