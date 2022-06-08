# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, UpdateView, DeleteView)

from .models import Persona
from .forms import EmpleadoForm


class InicioView(TemplateView):
    """Vista que carga la pagina de inicio"""
    template_name = 'inicio.html'


# Requerimientos
# 1 - Listar todos los empleados de la empresa
class ListAllEmployees(ListView):
    template_name = 'persona/list_all_employees.html'
    paginate_by = 4
    ordering = 'id'
    context_object_name = 'lista_empleados'
    # model = Persona  # se usa cunado no se usa get_queryset
    # context_object_name = 'empleados'

    # Sirve para retornar data y filtrar
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')

        # icontains: sirve como si fuera %like%
        lista = Persona.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista


class ListAllEmployeesAdmin(ListView):
    template_name = 'persona/list_all_employees_admin.html'
    paginate_by = 10
    ordering = 'id'
    context_object_name = 'lista_empleados'
    model = Persona


# 2 - Listar todos los empleados de la empresa que pertenecen a una area
class ListEmployeeByArea(ListView):
    template_name = 'persona/list_by_area.html'
    model = Persona
    # queryset = Persona.objects.filter(departamento__name='Departamento de Ingenieria')
    context_object_name = 'empleados'

    def get_queryset(self):
        area = self.kwargs['id']
        lista = Persona.objects.filter(departamento__name=area)

        return lista


# 3 - Listar todos los empleados de la empresa por trabajo
class ListEmployeeByJob(ListView):
    template_name = 'persona/list_by_job.html'
    model = Persona

    # Se usa cuando queremos recibir algun parametro por URL del frontend
    def get_queryset(self):
        job = self.kwargs['job']
        lista = Persona.objects.filter(job=job)

        return lista


# 4 - Listar todos los empleados de la empresa por palabra clave
class ListEmployeeByKeyword(ListView):
    """Listado de empleados por palabra clave"""
    template_name = 'persona/list_by_keyword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('keyword', '')

        lista = Persona.objects.filter(first_name=palabra_clave)
        return lista


# 5 - Listar habilidades de un empleado
class ListSkillsEmployee(ListView):
    template_name = 'persona/list_skills_employee.html'
    context_object_name = 'habilidades'
    model = Persona

    def get_queryset(self):
        empleado = Persona.objects.get(id=6)
        res = empleado.habilidades.all()
        return res


# Obligatoriamente se tiene que usar un PK para ver detalle de x registro
class EmpleadoDetailView(DetailView):
    model = Persona
    template_name = 'persona/details_employee.html'

    # Podemos enviar datos extras que no sean parte de un modelo
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context


# SE USA EN SU MAYORIA SOLO PARA GENERAR PLANTILLAS HTML
class SuccessView(TemplateView):
    template_name = 'persona/success.html'


# INICIO SECCION DE CRUD
class EmpleadoCreateView(CreateView):
    model = Persona
    template_name = 'persona/add.html'

    # Forma 1: en caso se usa el modelo
    # fields = ['first_name', 'last_name', 'job', 'avatar', 'departamento', 'habilidades']
    # Forma 2: obtener todos los campos del modelo para el formulario
    # fields = ('__all__')

    # Forma 3: usando un formulario personalizado
    form_class = EmpleadoForm

    # Requiere una url para redireccionar, asignando un . la pagina se recarga
    # success_url = '.'
    # success_url = '/success'  # No es buena practica
    success_url = reverse_lazy('empleados_app:lista_empleados_admin')

    def form_valid(self, form):
        # Logica del proceso
        # Commit=False: No guarda en la BD solo en memoria para despues guardar
        empleado = form.save(commit=False)
        empleado.full_name = f'{empleado.first_name} {empleado.last_name}'
        empleado.save()

        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Persona
    template_name = 'persona/update.html'
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']
    success_url = reverse_lazy('empleados_app:lista_empleados_admin')

    def form_valid(self, form):
        # Logica del proceso
        # Commit=False: No guarda en la BD solo en memoria para despues guardar
        empleado = form.save(commit=False)
        empleado.full_name = f'{empleado.first_name} {empleado.last_name}'
        empleado.save()

        return super(EmpleadoUpdateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        """Se usa cuando se quiere validar data antes de que se ejecute form_valid,
        detecta los datos antes de validarlos y guardar
        """
        self.object = self.get_object()
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)


class EmpleadoDeleteView(DeleteView):
    model = Persona
    template_name = 'persona/delete.html'
    success_url = reverse_lazy('empleados_app:lista_empleados_admin')

    # # https://ccbv.co.uk/projects/Django/4.0/django.views.generic.edit/DeleteView/
    # def delete(self, request, *args, **kwargs):
    #     """
    #     Call the delete() method on the fetched object and then redirect to the
    #     success URL.
    #     """
    #     self.object = self.get_object()
    #     success_url = self.get_success_url()
    #     self.object.delete()
    #     # return HttpResponseRedirect(success_url)
