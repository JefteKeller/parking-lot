from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Level
from .serializers import LevelSerializer


class CreateListLevelView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        input_serializer = LevelSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        new_level = Level.objects.create(**input_serializer.data)

        output_serializer = LevelSerializer(new_level)
        output_data = output_serializer.data

        output_data['available_spaces'] = {
            'available_motorcycle_spaces': output_data['motorcycle_spaces'],
            'available_car_spaces': output_data['car_spaces']
        }
        del output_data['motorcycle_spaces']
        del output_data['car_spaces']

        return Response(output_data, status=status.HTTP_201_CREATED)

    def get(self, request):
        queryset_levels = Level.objects.all()

        output_data = []
        for queryset in queryset_levels:
            level = LevelSerializer(queryset).data

            car_space_used = queryset.level_spaces.filter(
                variety='car').count()
            motorcycle_space_used = queryset.level_spaces.filter(
                variety='motorcycle').count()

            level['available_spaces'] = {
                'available_motorcycle_spaces':
                level['motorcycle_spaces'] - motorcycle_space_used,
                'available_car_spaces': level['car_spaces'] - car_space_used
            }
            del level['motorcycle_spaces']
            del level['car_spaces']

            output_data.append(level)

        return Response(output_data, status=status.HTTP_200_OK)
