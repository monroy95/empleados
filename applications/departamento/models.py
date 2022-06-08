from django.db import models


# Create your models here.
class Departamento(models.Model):
    # editable=False: No se puede editar en el admin
    name = models.CharField('Nombre', max_length=50, unique=True)
    # null=True si no hay valor se registra un null -> NULL
    short_name = models.CharField('Nombre Corto', max_length=25, blank=True, null=True)
    anulate = models.BooleanField('Anulado', default=False)

    # Con esto cambiamos el nombre que aparecera en el panel admin de django
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['name']  # Descendente -> ['-name']
        unique_together = ('name', 'short_name')  # No permite que se registren combinaciones de datos repetidos

    def __str__(self):
        # NOTA: Los PK Django los genera automaticamente si no lo queremos
        # modificar manualmente
        return f"{self.id} - {self.name} - {self.short_name}"
