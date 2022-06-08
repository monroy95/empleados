# from django.contrib import admin
from django.urls import path  # , include
from . import views


def desde_apps2(self):
    print("wenass")


# Nombre para todo el conjunto de urls
app_name = 'empleados_app'

urlpatterns = [
    # path('persona/', desde_apps2),
    path('', views.InicioView.as_view(), name='inicio'),
    path('listar-empleados/', views.ListAllEmployees.as_view(), name='listar_empleados'),
    path('listar-empleados-admin/', views.ListAllEmployeesAdmin.as_view(), name='lista_empleados_admin'),
    path('listar-por-area/<id>', views.ListEmployeeByArea.as_view(), name='listar_por_area'),
    path('listar-por-trabajo/<job>', views.ListEmployeeByJob.as_view()),
    path('buscar-empleado/', views.ListEmployeeByKeyword.as_view()),
    path('listar-habilidades/', views.ListSkillsEmployee.as_view()),
    path('ver-empleado/<pk>', views.EmpleadoDetailView.as_view(), name='ver_empleado'),
    path('crear-empleado/', views.EmpleadoCreateView.as_view(), name='crear_empleado'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('actualizar-empleado/<pk>', views.EmpleadoUpdateView.as_view(), name='modificar_empleado'),
    path('eliminar-empleado/<pk>', views.EmpleadoDeleteView.as_view(), name='eliminar_empleado'),
]
