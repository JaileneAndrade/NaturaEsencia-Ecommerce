from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_completo = models.CharField(max_length=150)
    email = models.EmailField()
    direccion = models.CharField(max_length=250)
    total = models.PositiveBigIntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.nombre_completo}"