from django.db import models
from math import log

from django.forms import ValidationError


class Airplane(models.Model):
    airplane_id = models.IntegerField(
        primary_key=True, unique=True)  # user defined id
    passenger_count = models.IntegerField()  # user defined passenger assumption

    @property
    def fuel_tank_capacity(self):
        return self.airplane_id * 200

    @property
    def fuel_consumption_per_minute(self):
        result = log(self.airplane_id * 0.8) + self.passenger_count * 0.002
        # set minimum fuel consumption to 0.01 to avoid unrealistic negative values of fuel consumption
        return round(max(result, 0.01), 2)

    @property
    def max_flight_time(self):
        if self.fuel_consumption_per_minute == 0:
            return None
        return round(self.fuel_tank_capacity / self.fuel_consumption_per_minute, 2)

    def save(self, *args, **kwargs):
        if self.airplane_id < 1:
            raise ValueError("airplane_id must be greater than 1")
        if self.passenger_count is None:
            raise ValueError("passenger_count cannot be null")
        if self.passenger_count <= 0:
            raise ValueError("passenger_count must be positive")
        self._recalculate_fuel_consumption_per_minute_and_max_flight_time()

        if self.fuel_consumption_per_minute <= 0 or self.max_flight_time <= 0:
            raise ValidationError(
                "Calculated fuel consumption per minute and max flight time must be non-negative. "
                "Please check your airplane ID and passenger count."
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Airplane ID: {self.airplane_id}, Passenger Count: {self.passenger_count}"

    def _recalculate_fuel_consumption_per_minute_and_max_flight_time(self):
        self._fuel_consumption_per_minute = self.fuel_consumption_per_minute
        self._max_flight_time = self.max_flight_time


class FlightLog(models.Model):
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.FloatField()
    departure_airport = models.CharField(max_length=100)
    arrival_airport = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Airplane ID: {self.airplane.airplane_id}, Flight Time: {self.flight_time}, Fuel Consumption: {self.fuel_consumption}, Fuel Left: {self.fuel_left}, Created At: {self.created_at}"
