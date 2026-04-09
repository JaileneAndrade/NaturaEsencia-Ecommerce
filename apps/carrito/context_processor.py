
def importe_total_carrito(request):
    total = 0
    cantidad_total = 0
    if request.user.is_authenticated or True:
        carrito = request.session.get('carrito', {})
        for key, value in carrito.items():
            cantidad_total += value
            
    return {
        'total_carrito': total,
        'cantidad_carrito': cantidad_total,
    }