from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.template import loader
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import AccessToken
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # token_data = serializer.get_token(user)
            return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    try:
        if request.method == 'POST':
            email = request.data.get('email')
            password = request.data.get('password')
            user = authenticate(email=email, password=password)
            if user:
                access_token = AccessToken.for_user(user)
                return Response({'access_token': str(access_token)}, status=status.HTTP_200_OK)
            else:
                return Response("User does not exists", status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response(str(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)
