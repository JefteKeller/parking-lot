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

        # TODO Implement business rules to select the space level for the Vehicle
        filtered_level = Level.objects.get(id=1)

        chosen_level_space = LevelSpace.objects.create(
            variety=request.data['vehicle_type'],
            level_name=filtered_level.name,
            level=filtered_level)

        registered_vehicle = Vehicle.objects.create(
            vehicle_type=request.data['vehicle_type'],
            license_plate=request.data['license_plate'],
            space=chosen_level_space)

        output_serializer = VehicleSerializer(registered_vehicle)

        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, vehicle_id=None):
        return Response('')
