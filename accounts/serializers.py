from rest_framework import serializers

from accounts.models import NormalUser
from plants.serializers import PlantSerializer


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormalUser
        fields = ['email', 'name', 'phone_number', 'password']


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class UserVerifyCodeSerializer(serializers.Serializer):
    code = serializers.IntegerField()


class UserSerializer(serializers.ModelSerializer):
    saved_plants = PlantSerializer(many=True)

    class Meta:
        model = NormalUser
        exclude = ['password']
