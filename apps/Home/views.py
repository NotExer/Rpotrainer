from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return render(request, "index/landing.html")


def entrenamiento_main(request):
    return render(request, "index/entrenamiento_main.html")

def asesorias_main(request):
    return render(request, "index/asesorias_main.html")

def nutricion_main(request):
    return render(request, "index/nutricion_main.html")

def sobre_main(request):
    return render(request, "index/sobre_main.html")

def testimonios_main(request):
    return render(request, "index/testimonios_main.html")

def contacto_main(request):
    return render(request, "index/contacto_main.html")