from django.contrib import admin

# Register your models here.

from viviendas.models import *

class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'apellido', 'cedula')
    search_fields = ('id','nombre', 'apellido', 'cedula')

admin.site.register(Propietario, PropietarioAdmin)

class EdificioAdmin(admin.ModelAdmin):

    list_display = ('id','nombre', 'direccion', 'ciudad', 'tipo')
    search_fields = ('id','nombre', 'direccion')

admin.site.register(Edificio, EdificioAdmin)


class DepartamentoAdmin(admin.ModelAdmin):

    list_display = ('id','propietario', 'costo', 'num_cuartos', 'edificio')

    search_fields = ('id','propietario','edificio')

admin.site.register(Departamento, DepartamentoAdmin)