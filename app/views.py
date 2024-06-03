from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Person, Car, BuyCar
from .serializers import PersonSerializer, CarSerializer, BuyCarSerializer
from .producers import send_car_buy_message

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]

class BuyCarViewSet(viewsets.ModelViewSet):
    queryset = BuyCar.objects.all()
    serializer_class = BuyCarSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        send_car_buy_message(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
