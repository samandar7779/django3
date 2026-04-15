from django.urls import path

from .views import home, car_detail

urlpatterns = [
    path('', home, name='home'),
    path('cars/<int:car_id>/', car_detail, name='detail'),

]