from rest_framework import serializers
from property_api.models import Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
class PropertyCreateUpdateSerializer(serializers.ModelSerializer):
     class Meta:
        model = Property
        fields = '__all__'