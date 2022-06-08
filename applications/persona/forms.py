from django import forms

from .models import Persona


class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ('first_name', 'last_name', 'job', 'departamento', 'avatar', 'habilidades',)
        widgets = {
            'habilidades': forms.CheckboxSelectMultiple(),
        }
