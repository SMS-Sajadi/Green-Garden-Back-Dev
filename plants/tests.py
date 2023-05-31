from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Plant

class MyModelTestCase(APITestCase):
    def setUp(self):
        # 'type', 'light_intensity', 'temperature', 'location_type', 'water', 'growth',
        # 'attention_need', 'season', 'is_seasonal', 'fragrance', 'pet_compatible',
        # 'allergy_compatible', 'edible'
        self.obj = Plant.objects.create(name="رز", description="گل", maintenance="خنک", type=1 , light_intensity=1 , water=3 , growth=1 , attention_need="متوسط" , season="همه" , is_seasonal="خ")

    def test_my_model_list(self):
        url = reverse('my-model-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_my_model_detail(self):
        url = reverse('my-model-detail', args=[self.obj.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'foo')
        self.assertEqual(response.data['description'], 'bar')