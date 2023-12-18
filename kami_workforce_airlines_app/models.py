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
        if self.airplane_id <= 1:
            raise ValueError("airplane_id must be greater than 1")
        if self.passenger_count is None:
            self.passenger_count = 1
        if self.passenger_count <= 0:
            raise ValueError("passenger_count must be positive")
        self._recalculate_fuel_consumption_per_minute_and_max_flight_time()

        if self.fuel_consumption_per_minute <= 0 or self.max_flight_time <= 0:
            raise ValueError(
                "Calculated fuel consumption per minute and max flight time must be positive."
            )
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Airplane ID: {self.airplane_id}, Passenger Count: {self.passenger_count}"

    def _recalculate_fuel_consumption_per_minute_and_max_flight_time(self):
        self._fuel_consumption_per_minute = self.fuel_consumption_per_minute
        self._max_flight_time = self.max_flight_time
