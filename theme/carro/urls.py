from django.urls import path
from django.conf.urls.static import static
from .views import agregar_producto, eliminar_producto, restar_producto, limpiar_carro

app_name = "carro"

urlpatterns = [
    path('agregar/<int:producto_id>/', agregar_producto, name='agregar'),
    path('eliminar/<int:producto_id>/', eliminar_producto, name='eliminar'),
    path('restar/<int:producto_id>/', restar_producto, name='restar'),
    path('limpiar/', limpiar_carro, name='limpiar'),
]