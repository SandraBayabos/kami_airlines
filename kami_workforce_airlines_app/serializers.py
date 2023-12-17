from rest_framework import serializers
from .models import Airplane
from typing import List, Dict


class AirplaneSerializer(serializers.Serializer):
    airplane_id = serializers.IntegerField()
    passenger_count = serializers.IntegerField()

    def create(self, validated_data: Dict[str, int]):
        return Airplane.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.airplane_id = validated_data.get(
            'airplane_id', instance.airplane_id)
        instance.passenger_count = validated_data.get(
            'passenger_count', instance.passenger_count)
        instance.save()
        return instance
    
    def validate_airplane_id(self, value): # check if airplane_id already exists in db
        if Airplane.objects.filter(airplane_id=value).exists():
            raise serializers.ValidationError("airplane_id already exists")
        return value
