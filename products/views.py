from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Category, Product
from .serializers import ProductListSerializer, ProductSerializer, CategorySerializer
from rest_framework import generics


# class CategoryView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer    # полностью весь крад
    
# class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return self.serializer_class