from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def boglanish(request):
    return render(request, 'contac.html')

def haqimizda(request):
    return render(request, 'haqida.html')

def manzil(request):
    return render(request, 'manzil.html')