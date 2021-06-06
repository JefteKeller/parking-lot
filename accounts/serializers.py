from rest_framework import serializers


class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=150, write_only=True)
    is_superuser = serializers.BooleanField()
    is_staff = serializers.BooleanField()
