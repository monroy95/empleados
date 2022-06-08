# from django.shortcuts import render
# from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView

from applications.persona.models import Persona

from .forms import NewDepartamentoForm
from .models import Departamento


# vista para departamentos
class DepartamentoListView(ListView):
    model = Departamento
    template_name = 'departamento/departamento_list.html'
    context_object_name = 'departamentos'


# Create your views here.
class NewDepartamento(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'  # reverse_lazy('departamento:list_departamento')

    def form_valid(self, form):
        # form.save()

        depa = Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['nombre_corto']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        Persona.objects.create(first_name=nombre, last_name=apellidos, job='1',
                               departamento=depa)

        return super().form_valid(form)
