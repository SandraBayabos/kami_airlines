from rest_framework import serializers
from .models import Airplane


class AirplaneSerializer(serializers.Serializer):
    airplane_id = serializers.IntegerField()
    passenger_count = serializers.IntegerField()

    def create(self, validated_data):
        return Airplane.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.airplane_id = validated_data.get(
            'airplane_id', instance.airplane_id)
        instance.passenger_count = validated_data.get(
            'passenger_count', instance.passenger_count)
        instance.save()
        return instance
