from rest_framework import serializers
from .models import Categoria, Evento
from .validators import validar_nombre


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'


class ReporteEventosSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    Eventos = EventoSerializer(many=True)


class ContactSerializer(serializers.Serializer):
    email = serializers.EmailField()
    subject = serializers.CharField(max_length=100, validators=[validar_nombre,])
    body = serializers.CharField(max_length=255)
