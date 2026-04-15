from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

cars = [
    {'id': 1, 'name': 'Malibu', 'brand': 'Chevrolet', 'price': 30000},
    {'id': 2, 'name': 'Cobalt', 'brand': 'Chevrolet', 'price': 15000},
    {'id': 3, 'name': 'Camry', 'brand': 'Toyota', 'price': 35000},
    {'id': 4, 'name': 'K5', 'brand': 'Kia', 'price': 32000}
]


def home(request):
    context={
        'cars':cars
    }
    return render(request, 'main/index.html', context)

def car_detail(requset, car_id):
    for car in cars:
        if car.get('id')==car_id:
            context={
                'car':car
            }
            return render(requset, 'main/detail.html', context)
    return  HttpResponse('Bunday kitob mavjud emas', status=400)


