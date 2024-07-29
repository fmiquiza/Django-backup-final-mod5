from django.db import models
from .validators import validar_par, validation_categoria, validar_fecha_futura
from django.core.validators import EmailValidator
from agenda import validators


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, validators=[validation_categoria,])

    def __str__(self):
        return self.nombre

    class Meta:
        permissions = [
            ('reporte_cantidad', 'Visualizar el reporte'),
            ('reporte_detalle', 'Reporte detallado'),
        ]
        
class Invitado(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Evento(models.Model):
    titulo = models.CharField(max_length=10, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()
    created = models.DateTimeField(validators=[validar_fecha_futura])
    updated = models.DateTimeField()
    disponible = models.BooleanField(blank=True, default=True)

    #invitado = models.ForeignKey(Invitado, on_delete=models.CASCADE)

    """ def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('La fecha de finalización debe ser después de la fecha de inicio.') """

    def __str__(self):
        return self.titulo

class EventoInvitado(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    invitado = models.ForeignKey(Invitado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.evento.titulo} - {self.invitado.nombre}"