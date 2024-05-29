from django.shortcuts import render
from product.models import Kinds,Product
from rest_framework import generics
from api.serializers import KindSerializers,ProductSerializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
# Create your views here.

class KindApiView(generics.ListAPIView):
    queryset = Kinds.objects.all()
    serializer_class = KindSerializers
    filter_backends = [SearchFilter]
    search_fields = ['kind']


class ProductApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ["knds_id","title"]
    search_fields = ['title','about']
    ordering_fields = ['price']




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