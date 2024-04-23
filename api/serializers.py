from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


# from rest_framework import serializers
# from .models import *
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'password']
        
        
#     def save(self, **kwargs):
#         new_user = User.objects.create_user(
#             username= self.validated_data['username'],
#             email= self.validated_data['email'],
#             password= self.validated_data['password']
#         )
        
#         new_user.save()
        
#         new_token = Token.objects.create(user=new_user)