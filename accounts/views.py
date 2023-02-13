from django.shortcuts import render
from rest_framework.views import APIView
from accounts.serializers import UserRegisterSerializer,UserSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth.models import User
# Create your views here.


class RegisterAPIView(APIView):
    serializer_class = UserRegisterSerializer
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            response_data =  {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user':serializer.data
            }
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserMeAPIView(APIView):
    def get(self,request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

class LogOutAPIView(APIView):
    def post(self, request, format=None):
        try:
            refresh_token = request.data("refresh_token")
            token_obj = RefreshToken(refresh_token)
            token_obj.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    