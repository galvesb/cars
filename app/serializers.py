from rest_framework import serializers
from .models import Person, Car, BuyCar

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'age']

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'model', 'owner']

class BuyCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyCar
        fields = ['id', 'person', 'car', 'message']
