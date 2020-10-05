from django.urls import path
from django.views.generic import TemplateView
from .views import Home, Articles, Create, Update, Delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('articles/<str:pk>', Articles.as_view(), name = 'articles'),
    path('create/', Create.as_view(), name = 'create'),
    path('update/<str:pk>', Update.as_view(), name = 'update'),
    path('delete/<str:pk>', Delete.as_view(), name = 'delete'),

    ] 
    #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)