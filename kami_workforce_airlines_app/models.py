from django.db import models
from math import log

class Airplane(models.Model):
    airplane_id = models.AutoField(primary_key=True)
    passenger_count = models.IntegerField()

    @property
    def fuel_tank_capacity(self):
        return self.airplane_id * 200
    
    @property
    def fuel_consumption_per_minute(self):
        return log(self.airplane_id * 0.8) + self.passenger_count * 0.002
    
    @property
    def max_flight_time(self):
        return self.fuel_tank_capacity / self.fuel_consumption_per_minute