from django.urls import path
from findCar.views import CreateCars, CreateCargo, FindCar, ListCargo, CarView, EditCarView, CargoView, EditCargoView

urlpatterns = [
    path('createCars/', CreateCars.as_view()),
    path('createCargo/', CreateCargo.as_view()),
    path('findCar/<int:cargo>', FindCar.as_view()),
    path('listCargo/', ListCargo.as_view()),
    path('car/', CarView.as_view()),
    path('car/<int:pk>', EditCarView.as_view()),

    path('cargo/', CargoView.as_view()),
    path('cargo/<int:pk>', EditCargoView.as_view()),
]
