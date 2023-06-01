from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from plants.models import Plant
from .models import NormalUser


class SavedPlantListTestCase(APITestCase):
    def setUp(self):
        self.user = NormalUser.objects.create_user(name='testuser', email='test@gmail.com', phone_number="09132541212",
                                                   password="1234")
        self.plant = Plant.objects.create(name="رز", description="گل", maintenance="در آب وایتکس ریخته شود", type=1,
                                          light_intensity=2,
                                          temperature=20, water=3, growth=1, attention_need=1, season=3,
                                          is_seasonal=False, fragrance=False, pet_compatible=True,
                                          allergy_compatible=True, edible=False, special_condition="ندارد",
                                          is_valid=True)
        self.url = reverse('accounts:saved_plant_list', kwargs={'id_plant': self.plant.id})

    def test_save_plant(self):
        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.user.saved_plants.filter(id=self.plant.id).exists())
