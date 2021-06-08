from rest_framework import serializers
# from rest_framework.validators import UniqueValidator

# from .models import Level


class LevelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField(
        max_length=150
        # validators=[UniqueValidator(queryset=Level.objects.all())])
    )
    fill_priority = serializers.IntegerField()
    motorcycle_spaces = serializers.IntegerField()
    car_spaces = serializers.IntegerField()


class LevelSpaceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    variety = serializers.CharField(max_length=150)
    level_name = serializers.CharField(max_length=150)
