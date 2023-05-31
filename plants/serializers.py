from rest_framework import serializers

from accounts.models import NormalUser
from .models import Plant, SavedPlantList


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'


class SavedPlantListSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=NormalUser.objects.all())
    plants = PlantSerializer(many=True)

    class Meta:
        model = SavedPlantList
        fields = '__all__'
