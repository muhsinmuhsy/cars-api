from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from rest_framework import status
from api.models import *
from api.serializers import *
from rest_framework import status

# Create your views here.


@api_view(['GET'])
def car_list(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class Signup(APIView):
    def post(self, request, Fomat=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data[' username'])
            token = Token.objects.get(user=user)
            
            serializer = UserSerializer(user)
            
            data = {
                "user": serializer.data,
                "token": token
            }
            return Response(data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    
class Login(APIView):
    def post(self, request, Fomat=None):
        pass
    
class TestView(APIView):
    def get(self, request, Fomat=None):
        pass