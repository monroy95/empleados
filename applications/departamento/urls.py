# from django.contrib import admin
from django.urls import path  # , include  # re_path
from . import views


# Nombre para todo el conjunto de urls
app_name = 'departamento_app'

urlpatterns = [
    path('new-departamento/', views.NewDepartamento.as_view(), name='new_departamento'),
    path('lista-departamentos/', views.DepartamentoListView.as_view(), name='lista_departamento'),
]
