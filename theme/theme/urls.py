"""theme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from django.views.generic.base import TemplateView

from django.views.static import serve # agregado para heroku
from django.conf.urls import url # agregado para heroku

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('orbital.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('postapi.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), # agregado para heroku
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), # agregado para heroku

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
