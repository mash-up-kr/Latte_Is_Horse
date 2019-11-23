from rest_framework import serializers

from beverages.models import Brand, Beverage


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'name',
            'image',
        )


class BeverageListSerializers(serializers.ModelSerializer):
    brand = BrandSerializer()

    class Meta:
        model = Beverage
        fields = (
            'beverage_name',
            'caffeine',
            'volume',
            'brand',
        )
