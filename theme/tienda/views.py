from .models import Producto
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView


# Create your views here.
class Tienda(TemplateView):

    template_name = "tienda/tienda.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.all()
        return context