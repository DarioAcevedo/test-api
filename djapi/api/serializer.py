from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Producto, categoria, subcategoria
from rest_framework.authtoken.models import Token
class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Producto
        fields= "__all__"

class categoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model= categoria
        fields= "__all__"

class subcategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model= subcategoria
        fields= "__all__"

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ('username', 'email', 'password')
        extra_kwargs = {'password':{'write_only': True}}
    def create(self, validated_data):
        user= User(
            email=validated_data['email'],
            username= validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user