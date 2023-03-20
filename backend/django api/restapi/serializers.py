from .models import Product,Category
from rest_framework import serializers,routers,viewsets
from drf_writable_nested import WritableNestedModelSerializer

class CategorySerializer(WritableNestedModelSerializer,serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id','kategori','deskripsi']

class ProductSerializer(WritableNestedModelSerializer,serializers.HyperlinkedModelSerializer):
   
    id_category = CategorySerializer()
    class Meta:
       model = Product
       fields = '__all__'