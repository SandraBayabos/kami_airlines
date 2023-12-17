from django.db import models
from math import log


class Airplane(models.Model):
    airplane_id = models.IntegerField(
        primary_key=True, unique=True)  # user defined id
    passenger_count = models.IntegerField()  # user defined passenger assumption

    @property
    def fuel_tank_capacity(self):
        return self.airplane_id * 200

    @property
    def fuel_consumption_per_minute(self):
        return round(log(self.airplane_id * 0.8) + self.passenger_count * 0.002, 2)

    @property
    def max_flight_time(self):
        return round(self.fuel_tank_capacity / self.fuel_consumption_per_minute, 2)

    def save(self, *args, **kwargs):
        if self.airplane_id <= 0:
            raise ValueError("airplane_id must be positive")
        if self.passenger_count <= 0:
            raise ValueError("passenger_count must be positive")
        if self.fuel_consumption_per_minute <= 0:
            raise ValueError(
                "fuel_consumption_per_minute must be positive. Ensure your passenger_count and airplane_id values are not too small.")
        if self.max_flight_time <= 0:
            raise ValueError(
                "max_flight_time must be positive. Ensure your passenger_count and airplane_id values are not too small.")
        super().save(*args, **kwargs)
