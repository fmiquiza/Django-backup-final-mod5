from django.contrib import admin
from .models import Categoria, Evento

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', )
    list_filter = ('categoria',)
    search_fields = ('titulo',)
    #ordering = ('precio',)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Evento, EventoAdmin)
