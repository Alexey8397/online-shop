from rest_framework import serializers
from myshop.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name" ,"slug", "image" ,"description", "price", "available", "created", "uploaded")
    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.available = validated_data.get('available', instance.available)
        instance.created = validated_data.get('created', instance.created)
        instance.uploaded = validated_data.get('uploaded', instance.uploaded)

        instance.save()
        return instance
