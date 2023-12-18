from django.test import TestCase
from .models import Airplane
from django.test import TestCase
import json


class AirplaneTestCase(TestCase):
    def setUp(self):
        Airplane.objects.create(airplane_id=100, passenger_count=100)
        Airplane.objects.create(airplane_id=200, passenger_count=200)
        Airplane.objects.create(airplane_id=300, passenger_count=300)
        Airplane.objects.create(airplane_id=400, passenger_count=400)

    def test_airplane_fuel_tank_capacity(self):
        airplane1 = Airplane.objects.get(airplane_id=100)
        airplane2 = Airplane.objects.get(airplane_id=200)
        self.assertEqual(airplane1.fuel_tank_capacity, 20000)
        self.assertEqual(airplane2.fuel_tank_capacity, 40000)

    def test_airplane_fuel_consumption_per_minute(self):
        airplane1 = Airplane.objects.get(airplane_id=100)
        airplane2 = Airplane.objects.get(airplane_id=200)
        self.assertEqual(airplane1.fuel_consumption_per_minute, 4.58)
        self.assertEqual(airplane2.fuel_consumption_per_minute, 5.48)

    def test_airplane_max_flight_time(self):
        airplane1 = Airplane.objects.get(airplane_id=100)
        airplane2 = Airplane.objects.get(airplane_id=200)
        self.assertEqual(airplane1.max_flight_time, 4366.81)
        self.assertEqual(airplane2.max_flight_time, 7299.27)

    def test_get_all_airplanes(self):
        response = self.client.get('/airlines/api/airplanes/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)

    def test_create_airplane(self):
        data = json.dumps([{'airplane_id': 600, 'passenger_count': 600}, {'airplane_id': 700, 'passenger_count': 700}, {'airplane_id': 800, 'passenger_count': 800},
                {'airplane_id': 900, 'passenger_count': 900}])
        response = self.client.post(
            '/airlines/api/airplanes/', data, content_type='application/json')
        print("Response Data:", response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data[0]['airplane_id'], 600)
        self.assertEqual(response.data[0]['passenger_count'], 600)
        self.assertEqual(response.data[1]['airplane_id'], 700)
        self.assertEqual(response.data[1]['passenger_count'], 700)
        self.assertEqual(response.data[2]['airplane_id'], 800)
        self.assertEqual(response.data[2]['passenger_count'], 800)
        self.assertEqual(response.data[3]['airplane_id'], 900)
        self.assertEqual(response.data[3]['passenger_count'], 900)

    def test_create_airplane_with_existing_airplane_id(self):
        data = json.dumps([{'airplane_id': 300, 'passenger_count': 300},
                {'airplane_id': 400, 'passenger_count': 400}])
        response = self.client.post(
            '/airlines/api/airplanes/', data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        error_message_found = any(
            'airplane_id already exists' in error_detail['airplane_id']
            for error_detail in response.data
            if 'airplane_id' in error_detail
        )
        self.assertTrue(error_message_found)

    def test_update_airplane(self):
        data = {'passenger_count': 300}
        response = self.client.patch(
            '/airlines/api/airplanes/100/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['airplane_id'], 100)
        self.assertEqual(response.data['passenger_count'], 300)
        self.assertEqual(response.data['fuel_consumption_per_minute'], 4.98)
        self.assertEqual(response.data['max_flight_time'], 4016.06)
