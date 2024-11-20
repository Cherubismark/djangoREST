from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ShopSerializers
from .models import Shop



# Create your views here.

class ShopViewset(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializers
