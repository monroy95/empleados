from django.contrib import admin
from .models import Persona, Habilidades


# Register your models here.
# admin.site.register(Persona)
admin.site.register(Habilidades)


# Personalizando el administrador
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name', 'last_name',
        'departamento', 'job',
        'full_name'  # columna personalizada
    )

    # Funcion personalizada para mostrar columna personalizada
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    # Agregando buscador
    search_fields = ('first_name',)
    list_filter = ('departamento', 'job', 'habilidades')

    # Agregando buscador en filtros se multiples selecciones
    filter_horizontal = ('habilidades',)


# Agregnado campos en list view
admin.site.register(Persona, EmpleadoAdmin)
