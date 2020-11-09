from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('thanks', views.thank, name='thank'),
    path('privacy', views.privacy, name='privacy'),
    ]