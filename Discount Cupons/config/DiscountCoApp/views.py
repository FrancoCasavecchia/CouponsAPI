from django.shortcuts import render
from rest_framework import viewsets

from .serializers import CouponsSerializer
from .models import Coupons

# Create your views here.

class CouponsViewSet(viewsets.ModelViewSet):
    queryset = Coupons.objects.all().order_by('code')
    serializer_class = CouponsSerializer