from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from apps.catalogo.models import Producto
from .models import Pedido

# Create your views here.

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    items_carrito = []
    total = 0

    for p_id, cantidad in carrito.items():
        producto = get_object_or_404(Producto, id=p_id)
        subtotal = producto.precio * cantidad
        total += subtotal
        items_carrito.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal,
        })
    return render(request, 'carrito.html', {
        'items_carrito': items_carrito,
        'total': total
    })

def agregar_al_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    
    p_id = str(producto_id)
    if p_id in carrito:
        carrito[p_id] += 1
    else:
        carrito[p_id] = 1
    request.session['carrito'] = carrito
    request.session.modified = True
    messages.success(request, 'Producto agregado al carrito.')

    return redirect('catalogo')

def restar_producto(request, producto_id):
    carrito = request.session.get('carrito', {})
    p_id = str(producto_id)
    if p_id in carrito:
        carrito[p_id] -= 1
        if carrito[p_id] < 1:
            del carrito[p_id]
    request.session['carrito'] = carrito
    request.session.modified = True
    return redirect('ver_carrito')

def sumar_producto(request, producto_id):
    carrito = request.session.get('carrito', {})
    p_id = str(producto_id)
    if p_id in carrito:
        carrito[p_id] += 1
    request.session['carrito'] = carrito
    request.session.modified = True
    return redirect('ver_carrito')

def eliminar_producto(request, producto_id):
    carrito = request.session.get('carrito', {})
    p_id = str(producto_id)
    if p_id in carrito:
        del carrito[p_id]
    request.session['carrito'] = carrito
    messages.error(request, "Producto eliminado.")
    return redirect('ver_carrito')

@login_required
def pago(request):
    carrito = request.session.get('carrito', {})
    if not carrito:
        messages.warning(request, "Tu carrito está vacío.")
        return redirect('catalogo')

    items_carrito = []
    total_pago = 0  # <--- Variable para sumar el total

    for p_id, cantidad in carrito.items():
        producto = get_object_or_404(Producto, id=p_id)
        subtotal = producto.precio * cantidad
        total_pago += subtotal  # <--- Sumamos cada subtotal al total
        
        items_carrito.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal,
        })

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')
        # Usamos el total_pago calculado aquí para mayor seguridad
        
        nuevo_pedido = Pedido.objects.create(
            usuario=request.user,
            nombre_completo=nombre,
            email=email,
            direccion=direccion,
            total=total_pago
        )

        request.session['carrito'] = {}
        request.session.modified = True
        
        return render(request, 'exito.html', {'pedido': nuevo_pedido})

    # Pasamos 'total_pago' al template
    return render(request, 'pago.html', {
        'items_carrito': items_carrito, 
        'total_pago': total_pago
    })