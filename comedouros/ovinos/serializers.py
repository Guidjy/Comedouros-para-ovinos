from rest_framework import serializers
from .models import Ovino


class OvinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ovino
        fields = '__all__'