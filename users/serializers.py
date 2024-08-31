from .models import User
from rest_framework import  serializers

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'phone_number', 'last_name', 'first_name']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number']
        extra_kwargs = {
            'image':{'required': False, }
        }

class LoginSerializer(serializers.Serializer):
    username_or_email = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=128)

class ResetPasswordSerializer(serializers.Serializer):
    old_password  = serializers.CharField(max_length=25)
    new_password = serializers.CharField(max_length=25)
