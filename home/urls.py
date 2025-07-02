from django.urls import path
from .views import home, boglanish,haqimizda,manzil

urlpatterns = [
    path('', home, name='home'),
    path('contac/', boglanish, name='contac'),
    path('haqida/', haqimizda, name='haqida'),
    path('manzil/', manzil, name='manzil')
]