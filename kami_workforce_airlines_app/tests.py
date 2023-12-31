from django.test import TestCase
from .models import Airplane
from django.test import TestCase
import json
from typing import Dict, Any


class AirplaneTestCase(TestCase):
    def setUp(self) -> None:
        Airplane.objects.create(airplane_id=100, passenger_count=100)
        Airplane.objects.create(airplane_id=200, passenger_count=200)

    def test_airplane_fuel_tank_capacity(self) -> None:
        airplane1 = Airplane.objects.get(airplane_id=100)
        airplane2 = Airplane.objects.get(airplane_id=200)
        self.assertEqual(airplane1.fuel_tank_capacity, 20000)
        self.assertEqual(airplane2.fuel_tank_capacity, 40000)

    def test_airplane_fuel_consumption_per_minute(self) -> None:
        airplane1 = Airplane.objects.get(airplane_id=100)
        airplane2 = Airplane.objects.get(airplane_id=200)
        self.assertEqual(airplane1.fuel_consumption_per_minute, 4.58)
        self.assertEqual(airplane2.fuel_consumption_per_minute, 5.48)

    def test_airplane_max_flight_time(self) -> None:
        airplane1 = Airplane.objects.get(airplane_id=100)
        airplane2 = Airplane.objects.get(airplane_id=200)
        self.assertEqual(airplane1.max_flight_time, 4366.81)
        self.assertEqual(airplane2.max_flight_time, 7299.27)

    def test_get_all_airplanes(self) -> None:
        response = self.client.get('/airlines/api/airplanes/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_create_airplane(self) -> None:  # test create 10 airplanes
        data: str = json.dumps([{'airplane_id': 300, 'passenger_count': 300}, {'airplane_id': 400, 'passenger_count': 400}, {'airplane_id': 500, 'passenger_count': 500}, {'airplane_id': 600, 'passenger_count': 600}, {'airplane_id': 700, 'passenger_count': 700}, {'airplane_id': 800, 'passenger_count': 800},
                                {'airplane_id': 900, 'passenger_count': 900}, {'airplane_id': 1000, 'passenger_count': 1000}, {'airplane_id': 1100, 'passenger_count': 1100}, {'airplane_id': 1200, 'passenger_count': 1200}])
        response = self.client.post(
            '/airlines/api/airplanes/', data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data[0]['airplane_id'], 300)
        self.assertEqual(response.data[0]['passenger_count'], 300)
        self.assertEqual(response.data[1]['airplane_id'], 400)
        self.assertEqual(response.data[1]['passenger_count'], 400)
        self.assertEqual(response.data[2]['airplane_id'], 500)
        self.assertEqual(response.data[2]['passenger_count'], 500)
        self.assertEqual(response.data[3]['airplane_id'], 600)
        self.assertEqual(response.data[3]['passenger_count'], 600)
        self.assertEqual(response.data[4]['airplane_id'], 700)
        self.assertEqual(response.data[4]['passenger_count'], 700)
        self.assertEqual(response.data[5]['airplane_id'], 800)
        self.assertEqual(response.data[5]['passenger_count'], 800)
        self.assertEqual(response.data[6]['airplane_id'], 900)
        self.assertEqual(response.data[6]['passenger_count'], 900)
        self.assertEqual(response.data[7]['airplane_id'], 1000)
        self.assertEqual(response.data[7]['passenger_count'], 1000)
        self.assertEqual(response.data[8]['airplane_id'], 1100)
        self.assertEqual(response.data[8]['passenger_count'], 1100)
        self.assertEqual(response.data[9]['airplane_id'], 1200)
        self.assertEqual(response.data[9]['passenger_count'], 1200)

    def test_create_airplane_with_existing_airplane_id(self) -> None:
        data: str = json.dumps([{'airplane_id': 100, 'passenger_count': 100},
                                {'airplane_id': 1300, 'passenger_count': 1300}])
        response = self.client.post(
            '/airlines/api/airplanes/', data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        error_message_found = any(
            'airplane_id already exists' in error_detail['airplane_id']
            for error_detail in response.data
            if 'airplane_id' in error_detail
        )
        self.assertTrue(error_message_found)

    def test_update_airplane(self) -> None:
        data: Dict[str, Any] = {'passenger_count': 300}
        response = self.client.patch(
            '/airlines/api/airplanes/100/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['airplane_id'], 100)
        self.assertEqual(response.data['passenger_count'], 300)
        self.assertEqual(response.data['fuel_consumption_per_minute'], 4.98)
        self.assertEqual(response.data['max_flight_time'], 4016.06)

    def test_delete_airplane(self) -> None:
        response = self.client.delete('/airlines/api/airplanes/100/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Airplane.objects.count(), 1)
        self.assertEqual(Airplane.objects.filter(airplane_id=100).count(), 0)

    def test_create_airplane_with_no_passenger_count(self) -> None:
        data: str = json.dumps([{'airplane_id': 1300}])
        response = self.client.post(
            '/airlines/api/airplanes/', data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        error_message_found = any(
            'This field is required.' in error_detail['passenger_count']
            for error_detail in response.data
            if 'passenger_count' in error_detail
        )
        self.assertTrue(error_message_found)

    def test_create_airplane_with_zero_passenger_count(self) -> None:
        data: str = json.dumps([{'airplane_id': 1300, 'passenger_count': 0}])
        response = self.client.post(
            '/airlines/api/airplanes/', data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        error_message_found = any(
            'passenger_count must be positive' in error_detail['passenger_count']
            for error_detail in response.data
            if 'passenger_count' in error_detail
        )
        self.assertTrue(error_message_found)
