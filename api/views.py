from django.shortcuts import render
from product.models import Kinds,Product
from rest_framework import generics
from api.serializers import KindSerializers,ProductSerializers

# Create your views here.

class KindApiView(generics.ListAPIView):
    queryset = Kinds.objects.all()
    serializer_class = KindSerializers

class ProductApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
# Create your views here.

class ProductCreateApiView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers





class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class KindCreateApiView(generics.CreateAPIView):
    queryset = Kinds.objects.all()
    serializer_class = KindSerializers


class KindRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kinds.objects.all()
    serializer_class = KindSerializers