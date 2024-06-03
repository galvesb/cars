from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Car(models.Model):
    model = models.CharField(max_length=100)
    owner = models.ForeignKey(Person, related_name='cars', on_delete=models.CASCADE)

    def __str__(self):
        return self.model

class BuyCar(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.person.name} bought {self.car.model}"
