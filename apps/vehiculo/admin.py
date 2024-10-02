from django.contrib import admin
from .models import Vehiculo, VehiculoImagen, ModeloFormularioBusqueda

# Personalización del sitio de administración
admin.site.site_header = "Cabrera Automotores"
admin.site.site_title = "Cabrera Automotores"


class VehiculoImagenInline(admin.TabularInline):
    model = VehiculoImagen
    extra = 1


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de vehículos
    list_display = ('marca', 'modelo', 'año',
                    'kilometraje')

    # Campos por los que se puede buscar en el panel de administración
    search_fields = ('marca', 'modelo', 'año', 'kilometraje')

    # Campos por los que se puede filtrar en el panel de administración
    list_filter = ('marca', 'modelo', 'año', 'kilometraje')

    # Agregar imágenes al panel de administración
    inlines = [VehiculoImagenInline]

    def kilometraje(self, obj):
        return f"{obj.kilometraje:,}".replace(',', '.')


@admin.register(ModeloFormularioBusqueda)
class ModeloFormularioBusquedaAdmin(admin.ModelAdmin):

    # Especifica los campos que se mostrarán en la lista de objetos del admin
    list_display = ('nombre_completo', 'marca', 'modelo', 'año_inicio',
                    'año_fin', 'numero_celular')

    # Permite la búsqueda a través de los campos especificados
    search_fields = ('marca', 'modelo', 'numero_celular')

    # Agrega filtros en la barra lateral para facilitar la búsqueda
    list_filter = ('marca', 'año_inicio', 'año_fin')
