from .models import Product,Category
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'categoryId', 'title', 'sell_price', 'full_price', 'image', 'rating']
        extra_kwargs = {
            'image': {'required': False}
        }
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']
    