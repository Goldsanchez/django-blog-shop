from django.urls import path
from django.views.generic import TemplateView
from .views import Home, Articles, Create, Update, Delete, Cash, Mtt, Spin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('articles/<str:pk>', Articles.as_view(), name = 'articles'),
    path('create/', Create.as_view(), name = 'create'),
    path('update/<str:pk>', Update.as_view(), name = 'update'),
    path('delete/<str:pk>', Delete.as_view(), name = 'delete'),
    path('cash/', Cash.as_view(), name = 'cash'),
    path('mtt/', Mtt.as_view(), name = 'mtt'),
    path('spin/', login_required(Spin.as_view()), name = 'spin'),

    ]