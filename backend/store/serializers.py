from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    rating = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'image', 'price',
                'qty', 'inventory', 'description', 'rating']