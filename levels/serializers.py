from rest_framework import serializers
# from rest_framework.validators import UniqueValidator

from .models import Level


class BaseLevelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField(
        max_length=150
        # validators=[UniqueValidator(queryset=Level.objects.all())])
    )
    fill_priority = serializers.IntegerField()


class LevelInputSerializer(BaseLevelSerializer):
    motorcycle_spaces = serializers.IntegerField()
    car_spaces = serializers.IntegerField()


class LevelOutputSerializer(BaseLevelSerializer):
    motorcycle_spaces = serializers.IntegerField(write_only=True)
    car_spaces = serializers.IntegerField(write_only=True)

    available_spaces = serializers.SerializerMethodField(
        'get_available_spaces', read_only=True)

    def get_available_spaces(self, level):
        queryset = Level.objects.get(id=level.id)

        motorcycle_space_used = queryset.level_spaces.filter(
            variety='motorcycle').count()
        car_space_used = queryset.level_spaces.filter(variety='car').count()

        available_motorcycle_spaces = queryset.motorcycle_spaces - motorcycle_space_used
        available_car_spaces = queryset.car_spaces - car_space_used

        return {
            'available_motorcycle_spaces': available_motorcycle_spaces,
            'available_car_spaces': available_car_spaces,
        }


class LevelSpaceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    variety = serializers.CharField(max_length=150)
    level_name = serializers.CharField(max_length=150)
