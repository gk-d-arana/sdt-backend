from rest_framework import serializers
from .models import *


class MainSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSection
        fields = '__all__'


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
