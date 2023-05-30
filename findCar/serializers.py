from rest_framework import serializers

from findCar.models import Cargo, Car


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class ListCargoSerializer(serializers.Serializer):
    weight = serializers.IntegerField()
    distance = serializers.IntegerField()

