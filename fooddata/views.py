from rest_framework.views import APIView
from rest_framework.response import Response
from fooddata.models import Food
from rest_framework import generics
from .serializers import FoodSerializer
from rest_framework.response import Response


class SearchFoods(generics.ListAPIView):
    serializer_class = FoodSerializer

    def get_queryset(self):

        searchtext = self.kwargs['searchtext']
        return Food.objects.filter(food_type__icontains=searchtext)

class RetrieveFood(generics.ListAPIView):
    serializer_class = FoodSerializer

    def get_queryset(self):

        fooditem = self.kwargs['fooditem']
        return Food.objects.filter(food_type=fooditem)       