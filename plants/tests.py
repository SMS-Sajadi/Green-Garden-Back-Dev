from rest_framework.test import APITestCase
from plants.serializers import PlantSerializer
from .models import Plant
from django.urls import reverse
from rest_framework import status


class PlantDetailsTestCase(APITestCase):
    def setUp(self):
        self.plant = Plant.objects.create(name="رز", description="گل", maintenance="در آب وایتکس ریخته شود", type=1,
                                        light_intensity=2,
                                        temperature=20, water=3, growth=1, attention_need=1, season=3,
                                        is_seasonal=False, fragrance=False, pet_compatible=True,
                                        allergy_compatible=True, edible=False, special_condition="ندارد", is_valid=True)
        self.url = reverse('plants:plant_details', kwargs={'id': self.plant.id})

    def test_get_valid_plant_details(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, PlantSerializer(self.plant).data)



