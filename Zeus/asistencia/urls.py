from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio , name='inicio'), #cuando vamos a acceder a una url vamos a usar este nombre
    path('nosotros/', views.nosotros, name='nosotros'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contactenos, name='contactenos'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('estudiantes/crear', views.crear, name='crear'),
    path('estudiantes/editar', views.editar, name='editar'),
]
