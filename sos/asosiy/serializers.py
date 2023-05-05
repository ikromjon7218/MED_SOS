from rest_framework import serializers
from .models import *

class InsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inson
        fields = '__all__'