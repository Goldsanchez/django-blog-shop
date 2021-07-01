from django.urls import path
from django.conf.urls.static import static
from .views import pokeApi

#app_name = "carro"

urlpatterns = [
    path('', pokeApi, name='pokeapi'),
]