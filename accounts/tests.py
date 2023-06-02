from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from plants.models import Plant
from .models import TemporaryUser, NormalUser

code = 0

class SavedPlantListTestCase(APITestCase):

    def setUp(self):
        self.valid_user_data = {
            'name': 'Mary',
            'email': 'Mary@example.com',
            'phone_number': '09132541212',
            'password': '1234'
        }
        self.user = NormalUser.objects.create_user(name='testuser', email='test@gmail.com', phone_number="09132541212",
                                                   password="1234")
        self.plant = Plant.objects.create(name="رز", description="گل", maintenance="در آب وایتکس ریخته شود", type=1,
                                          light_intensity=2,
                                          temperature=20, water=3, growth=1, attention_need=1, season=3,
                                          is_seasonal=False, fragrance=False, pet_compatible=True,
                                          allergy_compatible=True, edible=False, special_condition="ندارد",
                                          is_valid=True)

    def test_user_signup(self):
        url = reverse('accounts:user_register')
        response = self.client.post(url, data=self.valid_user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(TemporaryUser.objects.filter(email=self.valid_user_data['email']).exists())

    def test_save_plant(self):
        url = reverse('accounts:saved_plant_list', kwargs={'id_plant': self.plant.id})
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.user.saved_plants.filter(id=self.plant.id).exists())
