from rest_framework import serializers
from .models import Category, Product, ProductImage




class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'




class ProductSerializer(serializers.ModelSerializer):
    in_stock = serializers.BooleanField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instanse):
        representation = super().to_representation(instanse)
        # representation['images'] = ProductImageSerializer(instanse.images.all(), many=True).data
        representation['images'] = ProductImg(instanse.images.all(), many=True).data
        return representation




class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'image', 'price', 'category')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductImg(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = 'image',


