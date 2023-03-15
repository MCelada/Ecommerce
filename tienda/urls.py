from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar_producto/<int:producto_id>/', views.agregar_producto, name='agregar_producto'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('registrar/', views.registrar, name='registrar'),
    path('carrito/', views.carrito, name='carrito'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
]
