# from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
# importando modelos
from .models import Prueba
from .forms import PruebaForm


# Create your views here.
class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class PruebaListView(ListView):
    # model = MODEL_NAME
    template_name = "home/lista.html"
    context_object_name = 'my_list'
    queryset = ['1', '2', '3', '4', '5']


class ListarPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = 'my_list'


class PruebaCreateView(CreateView):
    template_name = "home/agregar.html"
    model = Prueba
    form_class = PruebaForm
    success_url = '/'
