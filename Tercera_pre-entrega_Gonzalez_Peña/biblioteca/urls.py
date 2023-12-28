from django.urls import path
from .views import lista_libros, agregar_libro

urlpatterns = [
    path('lista/', lista_libros, name='lista_libros'),
    path('agregar/', agregar_libro, name='agregar_libro'),
]
