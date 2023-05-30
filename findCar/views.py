import random
import string

from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from findCar.models import Car, Location, Cargo
from findCar.serializers import CargoSerializer, CarSerializer, ListCargoSerializer

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView


class CreateCars(APIView):
    @staticmethod
    def post(request):
        from findCar.service import graf
        graf.deleteGrafCars(Car.objects.all())
        Car.objects.all().delete()
        for i in range(0, 21):
            car = Car.objects.create(
                number=f"{random.randint(1000, 9999)}{random.choice(string.ascii_uppercase)}",
                current_location=Location.objects.order_by('?').first(),
                carrying_capacity=random.randrange(0, 10000),
            )
            car.save()
        graf.updateGrafCars(Car.objects.all())
        return Response(Car.objects.all().values())


class CreateCargo(APIView):
    @staticmethod
    @swagger_auto_schema(responses={200: CargoSerializer(many=False)})
    def post(request):
        from findCar.service import graf
        serializer = CargoSerializer(data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        cargo = Cargo.objects.create(**serializer.validated_data)
        graf.createCargo(cargo)
        return Response(CargoSerializer(instance=Cargo.objects.get(id=cargo.id), many=False).data)


class FindCar(APIView):
    @staticmethod
    def post(request, cargo):
        from findCar.service import graf
        cargo = get_object_or_404(Cargo, id=cargo)
        cars = graf.getCarsByCargo(cargo, int(request.query_params.get("radius", 450)))
        data = CargoSerializer(instance=cargo).data
        data["cars"] = list(Car.objects.filter(id__in=[node for node, _ in cars]).values())
        for c in range(len(cars)):
            data["cars"][c]["distance"] = cars[c][1]
        return Response(data)


class ListCargo(APIView):
    @staticmethod
    @swagger_auto_schema(responses={200: ListCargoSerializer(many=False)})
    def get(request):
        from findCar.service import graf
        cargo = Cargo.objects.all()
        data = []
        serializer = ListCargoSerializer(data=request.query_params, many=False)
        serializer.is_valid()
        serializer_data = serializer.validated_data
        weight = serializer.data.get('weight')
        distance = serializer_data.get('distance')

        for i in cargo:
            f = CargoSerializer(instance=i).data
            cars = graf.getCarsByCargo(i, int(request.query_params.get("radius", 450)))
            if len(cars) > 0:
                f["count"] = len(cars)
                f["nearest_car_id"] = cars[0][0]
                f["nearest_car_distance"] = cars[0][1]
                data.append(f)

        if distance:
            data = [cargo for cargo in data if cargo['nearest_car_distance'] <= int(distance)]

        if weight:
            weight = int(weight)
            if weight > 0:
                data = [cargo for cargo in data if cargo['weight'] <= weight]
            else:
                data = [cargo for cargo in data if cargo['weight'] >= weight]

        return Response(data)


class CarView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class EditCarView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def delete(self, request, pk):
        from findCar.service import graf
        graf.deleteGrafCar(self.queryset.get(pk=pk))
        self.queryset.get(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CargoView(ListAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


class EditCargoView(RetrieveUpdateDestroyAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

