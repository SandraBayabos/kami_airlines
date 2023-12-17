from django.test import TestCase
from .models import Airplane
from django.test import TestCase

class AirplaneTestCase(TestCase):
    def setUp(self):
        Airplane.objects.create(airplane_id=1, passenger_count=100)
        Airplane.objects.create(airplane_id=2, passenger_count=200)
        
    def test_airplane_fuel_tank_capacity(self):
        airplane1 = Airplane.objects.get(airplane_id=1)
        airplane2 = Airplane.objects.get(airplane_id=2)
        self.assertEqual(airplane1.fuel_tank_capacity, 200)
        self.assertEqual(airplane2.fuel_tank_capacity, 400)
        
    def test_airplane_fuel_consumption_per_minute(self):
        airplane1 = Airplane.objects.get(airplane_id=1)
        airplane2 = Airplane.objects.get(airplane_id=2)
        self.assertEqual(airplane1.fuel_consumption_per_minute, 0.1)
        self.assertEqual(airplane2.fuel_consumption_per_minute, 0.6)
        
    def test_airplane_max_flight_time(self):
        airplane1 = Airplane.objects.get(airplane_id=1)
        airplane2 = Airplane.objects.get(airplane_id=2)
        self.assertEqual(airplane1.max_flight_time, 2000)
        self.assertEqual(airplane2.max_flight_time, 666.67)

