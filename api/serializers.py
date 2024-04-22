from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        
        
    def save(self, **kwargs):
        new_user = User.objects.create_user(
            username= self.validated_data['username'],
            email= self.validated_data['email'],
            password= self.validated_data['password']
        )
        
        new_user.save()
        
        new_token = Token.objects.create(user=new_user)