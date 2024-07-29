from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Categoria, Evento
from .form import ProductForm
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import CategoriaSerializer, EventoSerializer, ReporteEventosSerializer, ContactSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import IsUserAlmacen
from .utils import permission_required
import logging


logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("Hola Mundo")

def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de hoy")

def categorias(request):
    post_titulo = request.POST.get("titulo")
    if post_titulo:
        q = Categoria(titulo=post_titulo)
        q.save()

    filtro_titulo = request.GET.get("titulo")
    if filtro_titulo:
        categorias = Categoria.objects.filter(titulo__contains=filtro_titulo)
    else:
        categorias = Categoria.objects.all()
    return render(request, "form_categorias.html", {"categorias": categorias})

def EventoFormView(request):
    form = ProductForm()
    Evento = None
    id_Evento = request.GET.get("id")
    if id_Evento:
        # Evento = Evento.objects.get(id=10011)
        Evento = get_object_or_404(Evento, id=id_Evento)
        form = ProductForm(instance=Evento)

    if request.method == "POST":
        if Evento:
            form = ProductForm(request.POST, instance=Evento)
        else:
            form = ProductForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, "form_Eventos.html", {"form": form})

# MODEL VIEW SET
class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# GENERIC API VIEW
class CategoriaCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

@api_view(['GET'])
def categoria_count(request):
    """
    Cuenta la cantidad de __categorias__
    """

    try:
        cantidad = Categoria.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )


@api_view(['GET'])
def Eventos_en_unidades(requesto):
    """
    Lista de Eventos filtrados en unidades
    """

    try:
        Eventos = Evento.objects.filter(unidades='u')
        return JsonResponse(
            EventoSerializer(Eventos, many=True).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )


@api_view(['GET'])
def reporte_Eventos(request):
    """
    Reporte de Eventos por categoria
    """

    try:
        Eventos = Evento.objects.filter(unidades='u')
        cantidad = Eventos.count()
        return JsonResponse(
            ReporteEventosSerializer({
                "cantidad": cantidad,
                "Eventos": Eventos
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )

