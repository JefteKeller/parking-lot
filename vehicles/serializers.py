from rest_framework import serializers

from levels.serializers import LevelSpaceSerializer


class VehicleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    license_plate = serializers.CharField(max_length=150)
    vehicle_type = serializers.CharField(max_length=150)

    arrived_at = serializers.DateTimeField(read_only=True)
    paid_at = serializers.DateTimeField(read_only=True, allow_null=True)
    amount_paid = serializers.IntegerField(read_only=True, allow_null=True)

    space = LevelSpaceSerializer(read_only=True)
