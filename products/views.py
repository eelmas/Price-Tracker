from django.shortcuts import render
from rest_framework import viewsets

from products.models import Product
from products.serializers import ProductSerializer


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

