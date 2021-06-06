from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User

from .serializers import AccountSerializer


class CreateAdminUserView(APIView):
    def post(self, request):
        input_serializer = AccountSerializer(data=request.data)

        input_serializer.is_valid(raise_exception=True)

        try:
            User.objects.get(username=request.data['username'])

            return Response({'message': 'User already exists'},
                            status=status.HTTP_409_CONFLICT)

        except User.DoesNotExist:
            new_user = User.objects.create_superuser(
                username=request.data['username'],
                password=request.data['password'])

        Token.objects.create(user=new_user)

        output_serializer = AccountSerializer(new_user)

        return Response(output_serializer.data, status=status.HTTP_201_CREATED)


class LoginAdminUserView(APIView):
    def post(self, request):

        found_user = authenticate(username=request.data['username'],
                                  password=request.data['password'])

        if not found_user:
            return Response({'message': 'Invalid credentials'},
                            status=status.HTTP_401_UNAUTHORIZED)

        user_token = Token.objects.get(user=found_user)

        return Response({'token': user_token.key}, status=status.HTTP_200_OK)
