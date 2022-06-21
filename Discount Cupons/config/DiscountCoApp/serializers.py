from rest_framework import serializers
from .models import Coupons

class CouponsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coupons
        fields = ('id','code','valid_from','valid_to','discount','active')