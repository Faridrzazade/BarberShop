from rest_framework import  serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BarberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barber
        fields = '__all__'

class SosialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SosialLinks
        fields = '__all__'