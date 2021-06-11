from django.shortcuts import get_object_or_404
from datetime import datetime, timezone

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from levels.models import Level, LevelSpace

from pricings.models import Pricing

from .models import Vehicle
from .serializers import VehicleSerializer


class CreateUpdateVehicleView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        VehicleSerializer(data=request.data).is_valid(raise_exception=True)

        recent_pricing = Pricing.objects.get_latest_pricing()

        if not recent_pricing:
            return Response({'error': 'There is not a base pricing set.'},
                            status=status.HTTP_404_NOT_FOUND)

        vehicle_type = request.data['vehicle_type']

        chosen_level = Level.get_available_level_by_priority(vehicle_type)

        if not chosen_level:
            return Response(
                {'error': 'There is not a Level or Space available.'},
                status=status.HTTP_404_NOT_FOUND)

        chosen_level_space = LevelSpace.objects.create(
            variety=vehicle_type,
            level_name=chosen_level.name,
            level=chosen_level)

        registered_vehicle = Vehicle.objects.create(
            vehicle_type=vehicle_type,
            license_plate=request.data['license_plate'],
            space=chosen_level_space)

        output_data = VehicleSerializer(registered_vehicle).data

        return Response(output_data, status=status.HTTP_201_CREATED)

    def put(self, request, vehicle_id=None):
        requested_vehicle = get_object_or_404(Vehicle, id=vehicle_id)

        recent_pricing = Pricing.objects.get_latest_pricing()

        if not recent_pricing:
            return Response({'error': 'There is not a base pricing set.'},
                            status=status.HTTP_404_NOT_FOUND)

        output_data = VehicleSerializer(requested_vehicle).data

        output_data[
            'amount_paid'] = requested_vehicle.calculate_vehicle_parking_bill(
                recent_pricing.a_coefficient, recent_pricing.b_coefficient)

        output_data['paid_at'] = datetime.now(timezone.utc)
        output_data['space'] = None
        del output_data['id']

        requested_vehicle.space.delete()
        requested_vehicle.delete()

        return Response(output_data, status=status.HTTP_200_OK)
