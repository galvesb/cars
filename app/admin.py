from django.contrib import admin
from . import models


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "age")


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "owner")


@admin.register(models.BuyCar)
class BuyCarAdmin(admin.ModelAdmin):
    list_display = ("person", "car", "message")
