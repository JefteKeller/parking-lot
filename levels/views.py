from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Level
from .serializers import LevelInputSerializer, LevelOutputSerializer


class CreateListLevelView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        input_serializer = LevelInputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        new_level = Level.objects.create(**input_serializer.data)

        output_serializer = LevelOutputSerializer(new_level)
        output_data = output_serializer.data

        return Response(output_data, status=status.HTTP_201_CREATED)

    def get(self, request):
        queryset_levels = Level.objects.all()

        output_data = LevelOutputSerializer(queryset_levels, many=True).data

        return Response(output_data, status=status.HTTP_200_OK)
