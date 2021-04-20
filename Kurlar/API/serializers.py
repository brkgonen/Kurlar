from rest_framework import serializers
from .models import Kurlar

class KurlarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Kurlar
        fields = '__all__'

