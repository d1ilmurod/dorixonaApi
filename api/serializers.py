from rest_framework import serializers
from product.models import Kinds,Product


class KindSerializers(serializers.ModelSerializer):

    class Meta:
        model = Kinds

        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


