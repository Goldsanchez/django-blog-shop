from django.urls import path
from django.conf.urls.static import static
from .views import Tienda


urlpatterns = [
    path('', Tienda.as_view(), name='tienda'),
]