from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from levels.models import Level, LevelSpace

from .models import Vehicle
from .serializers import VehicleSerializer


class CreateUpdateVehicleView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        input_serializer = VehicleSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        vehicle_type = request.data['vehicle_type']

        all_levels = Level.objects.all().order_by('fill_priority')
        chosen_level = None

        for level in all_levels:
            level_capacity = level.car_spaces if vehicle_type == 'car' else level.motorcycle_spaces

            if level.level_spaces.filter(
                    variety=vehicle_type).count() < level_capacity:

                chosen_level = level
                break

        if not chosen_level:
            return Response(
                {'error': 'There is not a Level or Space available.'},
                status=status.HTTP_404_NOT_FOUND)

        chosen_level_space = LevelSpace.objects.create(
            variety=request.data['vehicle_type'],
            level_name=chosen_level.name,
            level=chosen_level)

        registered_vehicle = Vehicle.objects.create(
            vehicle_type=request.data['vehicle_type'],
            license_plate=request.data['license_plate'],
            space=chosen_level_space)

        output_serializer = VehicleSerializer(registered_vehicle)

        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, vehicle_id=None):
        return Response('')
