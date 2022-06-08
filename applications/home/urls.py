from django.urls import path  # , include
from . import views


urlpatterns = [
    path('home/', views.PruebaView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.ListarPrueba.as_view()),
    path('lista-ingresar/', views.PruebaCreateView.as_view(), name='prueba_add'),
]
