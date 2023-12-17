from django.test import TestCase
from .models import Airplane
from django.test import TestCase
import json

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
        self.assertEqual(airplane1.fuel_consumption_per_minute, -0.02)
        self.assertEqual(airplane2.fuel_consumption_per_minute, 0.87)
        
    def test_airplane_max_flight_time(self):
        airplane1 = Airplane.objects.get(airplane_id=1)
        airplane2 = Airplane.objects.get(airplane_id=2)
        self.assertEqual(airplane1.max_flight_time, -10000.0)
        self.assertEqual(airplane2.max_flight_time, 459.77)
        
    def test_get_all_airplanes(self):
        response = self.client.get('/airlines/api/airplanes/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_create_airplane(self):
        data = json.dumps([{'airplane_id': 3, 'passenger_count': 300}])
        response = self.client.post('/airlines/api/airplanes/', data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data[0]['airplane_id'], 3)
        self.assertEqual(response.data[0]['passenger_count'], 300)
        self.assertEqual(response.data[0]['fuel_consumption_per_minute'], 1.48)
        self.assertEqual(response.data[0]['max_flight_time'], 405.41)