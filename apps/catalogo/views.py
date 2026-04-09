from django.shortcuts import render, redirect
from .models import Producto
from django.contrib import messages

def home(request):

    top_productos = Producto.objects.filter(disponible=True)[:3]
    return render(request, 'Mi_Ecommerce.html', {'top_productos': top_productos})

def catalogo_completo(request):

    productos = Producto.objects.filter(disponible=True)
    return render(request, 'catalogo.html', {'productos': productos})

def contacto(request):
    if request.method == "POST":
        messages.info(request, "Hemos recibido tu mensaje. Te contactaremos pronto.")
        return redirect('home')

    return render(request, 'contacto.html')




