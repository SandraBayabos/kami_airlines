from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Airplane
from .serializers import AirplaneSerializer


class AirplaneAPIView(APIView):
    def get(self, request):
        airplanes = Airplane.objects.all()
        serializer = AirplaneSerializer(airplanes, many=True)
        return Response(serializer.data)

    def post(self, request):  # handles multiple plane inputs
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
            print("airplane_data:", response)
            return Response(response, status=201)
        return Response(serializer.errors, status=400)
