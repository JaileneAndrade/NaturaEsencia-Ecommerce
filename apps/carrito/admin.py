from django.contrib import admin
from .models import Pedido

# Register your models here.

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    # Esto define qué columnas se ven en la tabla principal del admin
    list_display = ('id', 'nombre_completo', 'email', 'total', 'fecha_creacion')
    
    # Esto agrega un buscador por nombre o correo
    search_fields = ('nombre_completo', 'email')
    
    # Esto agrega un filtro lateral por fecha
    list_filter = ('fecha_creacion',)
    
    # Esto hace que los pedidos más nuevos aparezcan primero
    ordering = ('-fecha_creacion',)