from .models import Order
from rest_framework import serializers
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','user', 'product', 'qty', 'price', 'created_at', 'address','phone_number','description','status']    