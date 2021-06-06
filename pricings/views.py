from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Pricing
from .serializers import PricingSerializer


class CreatePricingView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        input_serializer = PricingSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        new_pricing = Pricing.objects.create(**input_serializer.data)
        output_serializer = PricingSerializer(new_pricing)

        return Response(output_serializer.data, status=status.HTTP_201_CREATED)
