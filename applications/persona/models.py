from ckeditor.fields import RichTextField
from django.db import models

from applications.departamento.models import Departamento


class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleado'

    def __str__(self):
        return f"{self.id} - {self.habilidad}"


# Create your models here.
class Persona(models.Model):
    """Modelo para tabla Persona"""
    JOB_TYPES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('Nombre Completo', max_length=120, blank=True)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_TYPES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', null=True, blank=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    # Con esto cambiamos el nombre que aparecera en el panel admin de django
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        # NOTA: Los PK Django los genera automaticamente si no lo queremos
        # modificar manualmente
        return f"{self.id} - {self.first_name} - {self.last_name}"
