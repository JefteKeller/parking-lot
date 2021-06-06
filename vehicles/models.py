from django.db import models

from levels.models import LevelSpace


class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=150)
    license_plate = models.CharField(max_length=150)

    arrived_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(default=None, blank=True, null=True)
    amount_paid = models.IntegerField(default=None, blank=True, null=True)

    space = models.ForeignKey(LevelSpace, on_delete=models.CASCADE)
