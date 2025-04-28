from rest_framework import serializers
from .models import cuaderno

class cuadernoSerializer(serializers.ModelSerializer):
    class Meta:
        model = cuaderno
        fields = '__all__'