
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from django.contrib.auth import authenticate, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.exceptions import ValidationError

class Signup(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = serializer.instance
            token, created = Token.objects.get_or_create(user=user)
            return Response({"user": serializer.data, "token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class Login(APIView):
    def post(self, request, format=None):
        data = request.data
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if user:
            serializer = UserSerializer(user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({"user": serializer.data, "token": token.key}, status=status.HTTP_200_OK)
        return Response({"details": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
    

# class TestView(APIView):
#     authentication_classes = [SessionAuthentication, TokenAuthentication]
#     permission_classes = [IsAuthenticated]
    
#     def get(self, request, format=None):
#         user = request.user
#         serialized_user = UserSerializer(user).data
#         return Response({"user": serialized_user, "message": "Test view"})

class TestView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        user = request.user
        user_data = {
            "username": user.username,
            "email": user.email,
        }
        return Response({"user": user_data, "message": "Test view"})


class Logout(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        try:
            request.user.auth_token.delete()
        except AttributeError:
            raise ValidationError("User has no auth_token.")
        logout(request)
        return Response({"message": "Logout was successful."})




# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, APIView
# from rest_framework import status
# from api.models import *
# from api.serializers import *
# from rest_framework import status
# from django.contrib.auth import authenticate, logout
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import SessionAuthentication, TokenAuthentication

# # Create your views here.


# class Signup(APIView):
#     def post(self, request, Fomat=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             user = User.objects.get(username=request.data['username'])

#             token = Token.objects.get(user=user)
            
#             serializer = UserSerializer(user)
            
#             data = {
#                 "user": serializer.data,
#                 "token": token.key
#             }
#             return Response(data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    
# class Login(APIView):
#     def post(self, request, Fomat=None):
#         data = request.data
#         authenticate_user = authenticate(username=data['username'], password=data['password'])
        
#         if authenticate_user is not None:
#             user = User.objects.get(username=data['username'])
#             serializer = UserSerializer(user)
            
            
#             response_data = {
#                 "user": serializer.data,
#             }
            
#             token, created_token = Token.objects.get_or_create(user=user)
            
#             if token:
#                 response_data['token'] = token.key
            
#             elif created_token:
#                 response_data['token'] = created_token.key
            
#             return Response(response_data, status=status.HTTP_201_CREATED)
#         return Response({"details":"not fount"}, status=status.HTTP_400_BAD_REQUEST)
    

# class TestView(APIView):
#     authentication_classes = [SessionAuthentication, TokenAuthentication]
#     permission_classes = [IsAuthenticated]
    
#     def get(self, request, format=None):
#         user = request.user
#         serialized_user = {
#             "id": user.id,
#             "username": user.username,
#             "email": user.email,
#         }
#         return Response({"user": serialized_user, "message": "Test view"})
    
    
# class Logout(APIView):
#     authentication_classes = [SessionAuthentication, TokenAuthentication]
#     permission_classes = [IsAuthenticated]
    
#     def get(self, request, format=None):
#         request.user.auth_token.delete()
#         logout(request)
#         return Response({"message": "Logt was Successfully"})