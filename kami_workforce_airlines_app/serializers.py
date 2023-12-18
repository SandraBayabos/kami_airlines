from rest_framework import serializers
from .models import Airplane
from typing import List, Dict


class AirplaneSerializer(serializers.Serializer):
    airplane_id = serializers.IntegerField()
    passenger_count = serializers.IntegerField()
    
    def create(self, validated_data):
        instance = Airplane(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        passenger_count = validated_data.get('passenger_count')
        if passenger_count is not None:
            if passenger_count < 1:
                raise serializers.ValidationError(
                    "passenger_count must be positive")
            else:
                instance.passenger_count = passenger_count

        instance.save()
        return instance

    # check if airplane_id already exists in db
    def validate_airplane_id(self, value):
        if Airplane.objects.filter(airplane_id=value).exists():
            raise serializers.ValidationError("airplane_id already exists")
        if value <= 0:
            raise serializers.ValidationError("airplane_id must be positive")
        return value

    # def validate_passenger_count(self, value):
    #     if value is None:
    #         print("passenger_count is None")
    #     if value <= 0:
    #         raise serializers.ValidationError(
    #             "passenger_count must be positive")
