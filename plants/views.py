from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from plants.serializers import PlantSerializer
from .models import Plant


class PlantFilterView(ListAPIView):
    serializer_class = PlantSerializer
    permission_classes = [AllowAny]
    # It can be safely remove if we only use get_queryset function
    queryset = Plant.objects.filter(is_valid=True)
    lookup_url_kwarg = ['type', 'light_intensity', 'temperature', 'location_type', 'water', 'growth',
                        'attention_need', 'season', 'is_seasonal', 'fragrance', 'pet_compatible',
                        'allergy_compatible', 'edible', ]

    def get_queryset(self):
        filter = {'is_valid': True}
        for field in self.lookup_url_kwarg:
            if self.request.query_params.get(field) and self.request.query_params[field] != '':
                filter[field] = self.request.query_params[field]
        return Plant.objects.filter(**filter)


class PlantDetailsView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = PlantSerializer
    queryset = Plant.objects.filter(is_valid=True)
    lookup_field = 'id'


class PlantListView(ListAPIView):
    serializer_class = PlantSerializer
    permission_classes = [AllowAny]
    queryset = Plant.objects.filter(is_valid=True)



