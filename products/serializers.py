from rest_framework import serializers
from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):

    in_stock = serializers.BooleanField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'image', 'price', 'category')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)



