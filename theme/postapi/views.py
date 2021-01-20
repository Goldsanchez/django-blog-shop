from django.shortcuts import render
from rest_framework import viewsets
from orbital.models import New
from .serializers import NewSerializer

# Create your views here.

class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer

#1. Install: pip install djangorestframework, en la carpea theme
# 2. crear una app para la api. ex: postapi
# 3. crear serializer.py e importar rest_framework y el modelo a serializar, en este caso New
# 4. en views.py importar viewsets, new and newserializer 
# 5. crear en urls.py el router e incluirlo