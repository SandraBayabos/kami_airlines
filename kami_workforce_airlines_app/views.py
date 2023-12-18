from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Airplane
from .serializers import AirplaneSerializer


class AirplaneAPIView(APIView):
    def get(self, request: Request) -> Response:
        airplanes = Airplane.objects.all()
        serializer = AirplaneSerializer(airplanes, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        unique_airplane_data = [item['airplane_id'] for item in request.data]

        if len(unique_airplane_data) != len(set(unique_airplane_data)):
            return Response({"error": "One or more airplane_id already exists"}, status=400)
        serializer = AirplaneSerializer(data=request.data, many=True)
        if serializer.is_valid():
            airplanes = serializer.save()
            response = [
                {
                    "airplane_id": airplane.airplane_id,
                    "passenger_count": airplane.passenger_count,
                    "fuel_consumption_per_minute": airplane.fuel_consumption_per_minute,
                    "max_flight_time": airplane.max_flight_time,
                } for airplane in airplanes
            ]
            print("Response:", response)
            return Response(response, status=201)
        else:
            print("Serializer Errors:", serializer.errors)
            return Response(serializer.errors, status=400)

    def patch(self, request: Request, airplane_id: int) -> Response:
        try:
            airplane = Airplane.objects.get(airplane_id=airplane_id)
        except Airplane.DoesNotExist:
            return Response({"error": "airplane_id does not exist"}, status=404)

        serializer = AirplaneSerializer(
            airplane, data=request.data, partial=True)
        if serializer.is_valid():
            airplane = serializer.update(airplane, request.data)

            print("Request Data:", request.data)
            if airplane:
                response = {
                    "airplane_id": airplane.airplane_id,
                    "passenger_count": airplane.passenger_count,
                    "fuel_consumption_per_minute": airplane.fuel_consumption_per_minute,
                    "max_flight_time": airplane.max_flight_time,
                }
                return Response(response, status=200)
            print("There was an issue with updating the data")

        print("Serializer Errors:", serializer.errors)
        return Response(serializer.errors, status=400)
